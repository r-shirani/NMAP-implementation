import socket
import struct
import time
import os
import select

#ICMP parameters
ICMP_ECHO_REQUEST = 8
ICMP_CODE = socket.getprotobyname("icmp")

def checksum(source_string):
    #checksum of the packet
    sum = 0
    count = 0
    count_to = (len(source_string) // 2) * 2
    while count < count_to:
        temp = source_string[count + 1] * 256 + source_string[count]
        sum = sum + temp
        sum = sum & 0xFFFFFFFF
        count += 2

    if count_to < len(source_string):
        sum = sum + source_string[len(source_string) - 1]
        sum = sum & 0xFFFFFFFF

    sum = (sum >> 16) + (sum & 0xFFFF)
    sum = sum + (sum >> 16)
    result = ~sum
    result = result & 0xFFFF
    result = result >> 8 | (result << 8 & 0xFF00)
    return result
