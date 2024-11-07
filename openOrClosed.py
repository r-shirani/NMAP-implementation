import socket

#ICMP parameters
ICMP_ECHO_REQUEST = 8
ICMP_CODE = socket.getprotobyname("icmp")

def port_status(host, port, timeout=1):
    #Check if a specific port is open
    try:
        destinationAddress = socket.gethostbyname(host)
    except socket.gaierror:
        print(f"Host {host} is unreachable (invalid hostname).")
        return

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((destinationAddress, port))#Zero if connected successfuly

    if result == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown service"
        print(f"open port detected: {host}\nport:{port}\nservice: {service}")
    #show the closed ports
    #else:
    #    print(f"Port {port} on {host} is closed or filtered.")

    sock.close()
    if result==0:#open port
        return 0
    return 1#closed port

def main():
    host = input("Enter the IP address: ")
    portRange = input("Enter the port range (e.g., 20-80): ")
    startPort, endPort = map(int, portRange.split('-'))
    isOpen=0#Zero if port connected successfuly,1 if not
    for port in range(startPort,endPort+1):
        isOpen+=port_status(host, port)
    if isOpen==(endPort-startPort+1):#none open port
        print("no open port was found")

if __name__ == '__main__':
    main()
