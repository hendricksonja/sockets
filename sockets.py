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
