import socket
import json
import threading
# Sample user data
users = {
    'user1': {'name': 'Alice', 'age': 30},
    'user2': {'name': 'Bob', 'age': 25},
    'user3': {'name': 'Charlie', 'age': 35},}

def handle_get_request(request):
    # Parse the request and extract the requested user ID
    request_parts = request.split()
    #correct format is--> GET user_id
    if len(request_parts) >= 2:
        user_id = request_parts[1]
        if user_id in users:
            user_info = json.dumps(users[user_id])
            response = f"HTTP/1.1 200 OK\nContent-Type: application/json\n\n{user_info}"
        else:
            response = "HTTP/1.1 404 Not Found\n\nUser not found"
    else:
        response = "HTTP/1.1 400 Bad Request\nContent-Type: application/json\n\n{\"error\": \"Invalid request format\"}"

    return response

def handle_post_request(request):
    command = request.split(' ')
    #correct format is--> POST user_name user_age
    if len(command)>=3:
        name = command[1]
        try:
            age = command[2]
            users[f'user{len(users)+1}'] = {'name': name, 'age': int(age)}
            response = f"HTTP/1.1 200 OK\nContent-Type: application/json\n\n{{\"message\": \"User created\", \"user_id\": \"{f'user{len(users)+1}'}\"}}"
        except ValueError:
            response = "HTTP/1.1 400 Bad Request\nContent-Type: application/json\n\n{\"error\": \"Age must be a number\"}"
    else:
        response = "HTTP/1.1 400 Bad Request\nContent-Type: application/json\n\n{\"error\": \"Invalid request format\"}"
    
    return response

def handle_client(client_socket):
    #receiving max 1024 byte data by converting it from binary to string
    request = client_socket.recv(1024).decode()
    if request.startswith("GET"):
        response = handle_get_request(request)
    elif request.startswith("POST"):
        response = handle_post_request(request)
    else:
        response = "HTTP/1.1 400 Bad Request\nContent-Type: application/json\n\n{\"error\": \"Invalid request method\"}"
    #send the response message by converting it from string to binary
    client_socket.sendall(response.encode())
    client_socket.close()

def main():
    host = 'localhost'
    port = 8080
    #TCP protocol
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#IPv4 protocol
    #socket connects to the certain port and host with bind function
    server_socket.bind((host, port))
    #acceptin maxiumum 5 connections
    server_socket.listen(5)
    print(f"Server is listening on http://{host}:{port}")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()


if __name__ == '__main__':
    main()
