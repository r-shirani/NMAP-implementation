import socket
import time

def delay(ip, port, numRequests):
    delays = []
    
    for i in range(numRequests):
        # Start time for the request
        startTime = time.time()
        
        # Create a connection to the specific port
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)  # Set a 2-second timeout for the connection
            sock.connect((ip, port))
            
            # End time after the connection is established
            endTime = time.time()
            
            # Calculate latency
            latency = endTime - startTime
            delays.append(endTime-startTime)
            
            # Close the connection
            sock.close()
        except socket.error as err:
            print(f"Error connecting to port {port}: {err}")
            delays.append(None)
    
    # Calculate the average delay
    if (latency for latency in delays if latency is not None):
        avg_latency = sum(delays) / len(delays)
        print(f"\nAverage delay for {numRequests} requests: {(avg_latency*1000):.4f} ms")
    else:
        print("No requests were successfully answered.")

def main():
    IP = input("Enter the IP address: ")
    port = int(input("Enter the port number: "))
    numRequests = int(input("Enter the number of requests: "))
    delay(IP, port, numRequests)


if __name__ == '__main__':
    main()
