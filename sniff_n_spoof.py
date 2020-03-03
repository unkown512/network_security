#!/usr/bin/python
from scapy.all import *
from random import randint

sniffed_dst_packets = {}

def sniff_stuff(packet):
  ip_layer=packet.getlayer(IP)
  #print(ip_layer)
  if(ip_layer):

    if(ip_layer.dst not in sniffed_dst_packets):
      sniffed_dst_packets[ip_layer.dst] = 1
    else:
      sniffed_dst_packets[ip_layer.dst] += 1


    spoof_packet = IP(ttl=64)
    sniffed_dst_packet_list = list(sniffed_dst_packets.keys())
    dst_range = len(sniffed_dst_packet_list)-1
    spoof_packet.src = sniffed_dst_packet_list[randint(0,dst_range)] 
    spoof_packet.dst = '199.199.199.199'#random_dst_ip
    send(spoof_packet)

packet = sniff(prn=sniff_stuff)
