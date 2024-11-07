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
def create_packet(ID):
    #Create an ICMP echo request packet
    # Dummy header with a 0 checksum
    """header = struct.pack("bbHHh", icmp_type, icmp_code, checksum, identifier, sequence)"""
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, 0, ID, 1)
    data = struct.pack("d", time.time())
    # Calculate the checksum on the header and data
    packet_checksum = checksum(header + data)
    # Construct the header again with the correct checksum
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, socket.htons(packet_checksum), ID, 1)
    return header + data
