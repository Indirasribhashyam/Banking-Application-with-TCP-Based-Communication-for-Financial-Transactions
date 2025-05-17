import socket

def create_tcp_connection(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
    except Exception as e:
        print("Connection error:", e)
        return None
    return s

def create_account(sock):
    username = input("Enter name: ")
    password = input("Set password: ")
    acc_id = input("Enter 5-digit account number: ")

    if not acc_id.isdigit() or len(acc_id) != 5:
        print("Account ID must be exactly 5 digits.")
        return

    msg = f"CREATE,{username},{password},{acc_id}"
    sock.send(msg.encode())
    print("Server:", sock.recv(1024).decode())

def login(sock):
    username = input("Username: ")
    password = input("Password: ")
    msg = f"LOGIN,{username},{password}"
    sock.send(msg.encode())
    print("Server:", sock.recv(1024).decode())

def perform_transaction(sock, cmd):
    acc_id = input("Account ID: ")
    password = input("Password: ")
    amount = "0"
    if cmd in ['1', '2', '5']:
        amount = input("Amount: ")

    msg = f"{cmd},{acc_id},{amount},{password}"
    sock.send(msg.encode())
    print("Server:", sock.recv(1024).decode())

def check_server_status(ip, port):
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_sock.sendto(b"STATUS_CHECK", (ip, port))
    response, _ = udp_sock.recvfrom(1024)
    print("UDP Response:", response.decode())
    udp_sock.close()

def main():
    server_ip = "127.0.0.1"  # Or change to actual IP
    tcp_port = 10001
    udp_port = 10002

    sock = create_tcp_connection(server_ip, tcp_port)
    if not sock:
        return

    while True:
        print("\n--- Banking Menu ---")
        print("1. Deposit")
        print("2. Withdrawal")
        print("3. Balance Inquiry")
        print("4. Create Account")
        print("5. Loan Request")
        print("6. Check Server Status")
        print("7. Close Account")
        print("8. Exit")

        choice = input("Choose: ")

        if choice == '4':
            create_account(sock)
        elif choice == '6':
            check_server_status(server_ip, udp_port)
        elif choice == '8':
            print("Exiting client.")
            sock.close()
            break
        elif choice in ['1', '2', '3', '5', '7']:
            perform_transaction(sock, 'CLOSE' if choice == '7' else choice)
        elif choice == 'LOGIN':
            login(sock)
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
