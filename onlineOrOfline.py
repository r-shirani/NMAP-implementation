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

def ping(host, timeout=1):
    #Send ICMP echo request and wait for a response
    try:
        # Resolve hostname to IP
        destinationAddress = socket.gethostbyname(host)
    except socket.gaierror:
        print(f"Host {host} is unreachable (invalid hostname).")
        return

    # Create raw socket for ICMP protocol
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, ICMP_CODE)
    except PermissionError:
        print("You need to run this script with administrative/root privileges.")
        return

    packet_id = os.getpid() & 0xFFFF
    packet = create_packet(packet_id)

    # Send the packet
    sock.sendto(packet, (destinationAddress, 1))
    # Wait for response
    start_time = time.time()
    while True:
        ready = select.select([sock], [], [], timeout)
        if ready[0] == []: # Timeout
            print(f"Request timed out for {host}.\nThe host is offline=(")
            return

        time_received = time.time()
        rec_packet, _ = sock.recvfrom(1024)

        # Check if the response is for the packet we sent
        icmp_header = rec_packet[20:28]
        _, _, _, recv_id, _ = struct.unpack("bbHHh", icmp_header)
        if recv_id == packet_id:
            echoTime = (time_received - start_time) * 1000 # in ms
            print(f"Ping of {host} is:{echoTime:.2f} ms\n The host is online=)")
            return

if __name__ == '__main__':
    servers = ["lms.ui.ac.ir", "golestan.ui.ac.ir", "stackoverflow.com","185.237.84.37 ","google.com"]
    for server in servers:
        ping(server)
