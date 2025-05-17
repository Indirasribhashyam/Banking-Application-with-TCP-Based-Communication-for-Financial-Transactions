import socket
import threading

accounts = {}

def tcp_client_handler(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode().strip()
            if not data:
                break

            parts = data.split(',')
            cmd = parts[0]

            if cmd == "CREATE":
                username, password, acc_id = parts[1], parts[2], parts[3]
                if acc_id in accounts:
                    client_socket.send(b"Account already exists.\n")
                else:
                    accounts[acc_id] = {"name": username, "password": password, "balance": 0, "limit": 10000}
                    client_socket.send(b"Account created successfully.\n")

            elif cmd == "LOGIN":
                username, password = parts[1], parts[2]
                found = False
                for acc_id, info in accounts.items():
                    if info["name"] == username and info["password"] == password:
                        found = True
                        client_socket.send(f"Login successful for account {acc_id}\n".encode())
                        break
                if not found:
                    client_socket.send(b"Login failed.\n")

            elif cmd in ['1', '2', '3', '5', 'CLOSE']:
                acc_id, amount, password = parts[1], parts[2], parts[3]
                if acc_id not in accounts:
                    client_socket.send(b"Invalid account ID.\n")
                    continue
                if accounts[acc_id]["password"] != password:
                    client_socket.send(b"Wrong password.\n")
                    continue

                if cmd == '1':  # Deposit
                    amt = int(amount)
                    accounts[acc_id]["balance"] += amt
                    client_socket.send(f"Deposit successful. Balance: {accounts[acc_id]['balance']}\n".encode())

                elif cmd == '2':  # Withdraw
                    amt = int(amount)
                    if amt > accounts[acc_id]["balance"]:
                        client_socket.send(b"Insufficient funds.\n")
                    elif amt > accounts[acc_id]["limit"]:
                        client_socket.send(b"Exceeds withdrawal limit.\n")
                    else:
                        accounts[acc_id]["balance"] -= amt
                        client_socket.send(f"Withdrawal successful. Balance: {accounts[acc_id]['balance']}\n".encode())

                elif cmd == '3':  # Balance Inquiry
                    client_socket.send(f"Your balance is {accounts[acc_id]['balance']}\n".encode())

                elif cmd == '5':  # Loan request (just a dummy response)
                    client_socket.send(b"Loan request received. Under review.\n")

                elif cmd == 'CLOSE':
                    del accounts[acc_id]
                    client_socket.send(b"Account closed successfully.\n")

        except Exception as e:
            print(f"Error: {e}")
            break

    client_socket.close()

def udp_status_server():
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_sock.bind(('0.0.0.0', 10002))
    print("UDP status server running on port 10002...")
    while True:
        msg, addr = udp_sock.recvfrom(1024)
        if msg.decode().strip() == "STATUS_CHECK":
            udp_sock.sendto(b"Server is up and running!", addr)

def start_server():
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind(('0.0.0.0', 10001))
    tcp_server.listen(5)
    print("TCP server listening on port 10001...")

    threading.Thread(target=udp_status_server, daemon=True).start()

    while True:
        client_sock, addr = tcp_server.accept()
        print(f"Connection from {addr}")
        threading.Thread(target=tcp_client_handler, args=(client_sock,)).start()

if __name__ == '__main__':
    start_server()
