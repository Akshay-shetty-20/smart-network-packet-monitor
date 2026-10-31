import socket

HOST = "0.0.0.0"
PORT = 5005

receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver.bind((HOST, PORT))

print("Smart Network Packet Monitor")
print("Waiting for ESP32 messages...")

while True:
    data, address = receiver.recvfrom(1024)
    message = data.decode()

    print(f"Received from {address}: {message}")

    if message.startswith("SEQ="):
        sequence_number = message.split("=")[1]
        acknowledgement = f"ACK={sequence_number}"

        receiver.sendto(acknowledgement.encode(), address)
        print(f"Sent acknowledgement: {acknowledgement}")
