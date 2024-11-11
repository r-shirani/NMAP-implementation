**Phase 1: Implementing Nmap Software Features**

Nmap is a highly powerful tool network administrators, security experts, and even hackers use to explore, analyze, and better understand computer networks. The name "Nmap" stands for "Network Mapper." This tool helps users find active devices on a computer network, identify services and applications running on those devices, and even detect security vulnerabilities.

For more information on this tool, you can refer to this link.
https://nmap.org/

It is recommended to download and install the software to become more familiar with it and try out some of its basic features. You can also try out certain features online and see the results by using this link to view how the tool works.
https://nmap.online/

#### Required Definitions

While reading this document, you might need some definitions. To make it easier for you, some of these definitions are provided below:

- **Host**: In the context of computer networks, a host refers to a device or system capable of connecting to a network. A host can be a computer, server, router, gateway, or similar. Each host in the network is assigned a unique IP address.

- **Service**: In network terminology, a service is a functionality provided by specific software or protocol running on a host in the network, offering certain services to other devices on the network.

- **Port**: In computer networks, a port is a number from 0 to 65535 used to identify services and applications. Each port typically corresponds to a specific service or application on a host, enabling communication and data exchange with other hosts in the network.
  - **Open Port**: If a port on a host is open, it means that the device responds to incoming requests on this port, allowing connections through it.
  - **Closed Port**: In contrast, if a port is closed on a host, it indicates that the host will not respond to incoming requests on this port, preventing connection through it.

### Project Objective

In this project, after learning some of the features of Nmap software, we are expected to implement some of its basic functionalities.

#### Required Features for Implementation

The implemented program should be able to perform the following tasks after receiving the target IP address and a range of ports to be scanned:

- Check whether a host is online or offline.
- Scan a range of ports on a host and report any open ports.
- Measure the response delay time for ports.
- Simulate the GET and POST methods of the HTTP protocol.

All the required functionalities can be implemented through socket programming. The following provides an overview of each requested feature.

##### Checking if a Host is Online or Offline

To implement this feature, the program should attempt to establish a connection with the specified host. If the connection is successfully established, the host is online; otherwise, the host is considered offline.

##### Port Scanning

The program should, after receiving the IP address of a host and a range of ports to be scanned, examine each port individually. If the port is open, it should return the port number and the service running on that port.

##### Measuring Port Response Delay

The program should be able to calculate the average response delay for a specified port. This average should be measurable for various request counts. For example, the average response delay for *n* sent requests.

##### Simulating GET and POST Methods

GET and POST are HTTP protocol request methods. GET is used for data retrieval, and POST is used to submit new data.

In this implemented program, we should enable the tool to retrieve user information by their ID using the GET method. The IDs are in the first column and include values like `user1`, `user2`, and `user3`. The acceptable format for the server program is as follows:
```
GET user_id
```
By entering the desired user ID, you can view that user’s information.

Additionally, the tool should have the capability to add a user’s information to the set of users using the POST method and by receiving the user’s name and age. The acceptable format for the server program is:
```
POST user_name user_age
```
The POST command will create a unique ID for each new user in the format `{last created user number + 1} + user`.
