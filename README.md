Below is a complete project document that includes both the assignment requirements with skeleton code (one file) for your students’ TCP/UDP client programs, as well as a full server (listener) program that you can host for testing.

---

# Socket Programming Assignment: TCP and UDP Clients

## Overview

In this assignment, you will create two Python client programs—one using TCP and one using UDP—to communicate with a server that implements a simple application-layer protocol. Both clients will use your school username as the payload. The server will validate your username (which may contain only letters, numbers, and underscores), generate a SHA‑256 hash of the username, and return it to you. This assignment will help you understand:

- The difference between TCP (connection-oriented) and UDP (connectionless) communication.
- Basic protocol design and how to enforce message order and format.
- How to build reliable client–server applications using Python’s socket API.

## Protocol Details

### TCP Client Protocol

Your TCP client should follow these steps:
1. **HELLO:** Send the message `"HELLO"` to initiate communication.
2. **ACK:** The server will respond with `"ACK:HELLO"`.
3. **DATA:** Send your username in the format `"DATA: <username>"` (for example, `"DATA: jhendrickson"`).
   - The server will validate the username and, if valid, generate a SHA‑256 hash.
   - The server will then respond with `"HASH:<hash>"` where `<hash>` is the hexadecimal hash value.
4. **BYE:** Send `"BYE"` to terminate the session.
5. **ACK:** The server will finish the conversation with `"ACK:BYE"`.

### UDP Client Protocol

Your UDP client will be simpler:
1. Send your username (e.g., `"jhendrickson"`) as a single message.
2. The server will validate the username and, if valid, reply with `"HASH:<hash>"`.

---

## Student Skeleton Code (Single File)

Below is a combined Python file that includes both TCP and UDP client skeletons. You are expected to complete and refine this code as needed.

```python
#!/usr/bin/env python3
"""
Socket Programming Assignment: TCP and UDP Clients

This script contains skeleton code for both TCP and UDP client applications.
Follow the protocol steps and use your school username as the payload.
"""

import socket

# ------------------------- UDP Client Code -------------------------
def udp_client(username):
    # Server details (update the HOST and PORT with your instructor's server info)
    HOST = '24.199.100.254'  # e.g., "192.0.2.1" or "example.com"
    PORT = 54321                  # UDP port
    timeout_duration = 2          # seconds

    try:
        # Create a UDP socket.
        
            # Set the socket timeout duration.
            
            
            # Send the username directly as the message.
            print(f"[UDP] Sending username: {username}")
            

            # Wait for the server response.
            
            
            # Decode and strip the response.
            
            
            # Check if the response starts with "HASH:".
            
            
            # Print the received response.
            print(f"[UDP] Received: {response}")

    except socket.timeout:
        # Handle the case where the request times out.
        print("[UDP] Request timed out.")
    except Exception as e:
        # Handle any other exceptions that occur.
        print(f"[UDP] An error occurred: {e}")

# ------------------------- TCP Client Code -------------------------
def tcp_client(username):
    # Server details (update the HOST and PORT with your instructor's server info)
    HOST = '24.199.100.254'  # e.g., "192.0.2.1" or "example.com"
    PORT = 12345                  # TCP port

    try:
        # Establish a TCP endpoint.
        with 
            # Connect to the remote server.
            

            # Step 1: Begin handshake by sending a starting message.
            
            # Wait for the acknowledgement of the handshake.
            
            if response != "ACK:HELLO":
                print(f"[TCP] Unexpected response: {response}")
                return
            print(f"[TCP] Received: {response}")

            # Step 2: Forward the identifier information.
            
            # Await and process the response containing validation details.
            
            if not response.startswith("HASH:"):
                print(f"[TCP] Error or invalid response: {response}")
                return
            print(f"[TCP] Received: {response}")

            # Step 3: Conclude the protocol by sending a termination message.
            
            # Wait for confirmation of session closure.
            
            if response != "ACK:BYE":
                print(f"[TCP] Unexpected termination response: {response}")
                return
            print(f"[TCP] Received: {response}")
            print("[TCP] Connection closed successfully.")

    except Exception as e:
        # Handle any issues encountered during the session.
        print(f"[TCP] An error occurred: {e}")



# ------------------------- Main Function -------------------------
def main():
    # Replace with your actual school username.
    username = input("Enter your school username: ").strip()

    protocol = input("Choose protocol (TCP/UDP): ").strip().upper()
    if protocol == "TCP":
        tcp_client(username)
    elif protocol == "UDP":
        udp_client(username)
    else:
        print("Invalid protocol selected. Please choose either TCP or UDP.")

if __name__ == '__main__':
    main()

```

### Submission Requirements

- **Source Code:**  
  Submit your completed Python file.
  
- **Documentation:**  
  Provide a brief report (300–500 words) explaining:
  - How your client works.
  - The differences between TCP and UDP.
  - Any challenges you encountered while implementing the protocol.
  
- **Demonstration:**  
  Include screenshots or logs showing successful connections to the provided server for both TCP and UDP protocols.  The below is an example:

  <img width="722" alt="image" src="https://github.com/user-attachments/assets/fb870ebe-374f-4b00-85b7-6b08be52efc7" />


---

## Summary
 
You are to implement client applications using the provided skeleton code. Ensure that your TCP client follows the multi-step protocol (sending `"HELLO"`, `"DATA: <username>"`, and `"BYE"` in sequence) and that your UDP client sends your username correctly. Test your programs locally before connecting to the instructor’s server.


Good luck with your assignment, and happy coding!
