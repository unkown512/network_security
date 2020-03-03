from scapy.all import *
import sys

# Sniffer
#sniff(prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:%Raw. load%\n}"))

# Send ICMP
src_ip = sys.argv[1]
dst_ip = sys.argv[2]
send(IP(src="IP", dst="IP")/ICMP()/"Hello World")
