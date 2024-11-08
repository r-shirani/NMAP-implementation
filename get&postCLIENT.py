import socket

def main():
    host = 'localhost'
    port = 8080
    while True:
        input=input("Enter 'GET user_id' or 'POST user_name user_age': ")
        #creating a socket and connect it to the host
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        #send the request to the server by converting it from string to binary
        client_socket.sendall(input.encode())
        #recieve the response
        response = client_socket.recv(1024).decode()
        #show the response
        print(f"Response from the server: {response}")
        #closing the socket
        client_socket.close()

if __name__ == '__main__':
    main()

