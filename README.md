# Banking-Application-with-TCP-Based-Communication-for-Financial-Transactions
The Financial Systems and Banking Software project is aimed at developing a secure and robust application for processing transactions, managing account data, and ensuring reliable communication between financial institutions.

## Table of Contents
- [Project Description](#project-description)
- [Functionalities](#functionalities)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [PPT](#ppt)

## Project Description

The application will leverage transport protocols, specifically TCP, to provide reliable, high-performance, and secure data transfer across the banking network. The design focuses on creating a stable environment for high-stakes data transfer, ensuring compliance with security standards, and optimizing transaction handling.This system will encompass critical features such as transaction processing, data security, and error handling. Financial transactions will be managed efficiently with precise data integrity checks, utilizing encryption techniques to protect sensitive information. The banking software will connect with external financial entities via secure protocols, facilitating the exchange of data such as payment requests, account updates, and fund transfers.

## Functionalities

1. Transaction Processing : Handles the execution of financial transactions, ensuring they are processed reliably and accurately. This module is crucial for maintaining the integrity and consistency of account data.
* User Side: Initiates transactions like transfers, payments, or withdrawals through a banking interface.
* Server Side: Processes transactions by updating account balances and ensuring ACID properties, logging each transaction for consistency.

2. Data Security: Protects sensitive information by encrypting communications and implementing secure authentication methods. Security measures include SSL/TLS encryption and secure key management.
* User Side: Enters sensitive data (e.g., passwords, personal info) via encrypted forms.
* Server Side: Encrypts data at rest and in transit using SSL/TLS, manages encryption keys, and enforces secure data storage.


3. Account Management: Manages user accounts, including data retrieval and updates, ensuring only authorized access is granted.
*	User Side: Accesses account information, updates personal details, or performs transactions.
*	Server Side: Retrieves and updates account data from the database, enforcing access controls to ensure only authorized changes are made.


4. Communication with External Systems: Integrates with other financial institutions and payment networks, such as SWIFT, to send and receive transaction data securely.
*	User Side: Requests transactions involving external accounts or services (e.g., wire transfers).
*	Server Side: Interfaces with external financial systems (e.g., SWIFT) to securely send and receive transaction data.


5. Error Handling and Logging: Monitors transactions and system operations, providing error detection and logging capabilities for troubleshooting and auditing.
*	User Side: Receives notifications or alerts in case of errors during transactions.
*	Server Side: Detects and logs errors during transactions, triggering retry mechanisms or notifying administrators.

6. User Authentication and Access Control:
Manages the verification of user identities using methods like passwords,     biometrics, and two-factor authentication (2FA).
*	User Side: Logs in using passwords, biometrics, or 2FA to access banking services.
*	Server Side: Verifies user credentials, assigns roles, and grants access based on user permissions.


## System Requirements

- Python 3.7 or above
- OS: Linux / Windows / macOS
- Open network ports: `9999` (Server) and `10001` (Client)
- Wireshark (optional, for network traffic analysis)


## Installation

Clone the repository:
```bash
git clone https://github.com/Indirasribhashyam/Banking-Application-with-TCP-Based-Communication-for-Financial-Transactions.git
cd banking-tcp-app
```

## Running the Project

### 1. Run the Server

To run the server, execute the following command on the **server VM**:

```bash
python3 server.py
```

The server will start listening on port 9999. *The IP address used in the code should be updated to match the server VM's IP.*

### 2. Run the Client

To simulate multiple clients, run the following command on each **client VM**:

```bash
python3 client.py
```




## PPT
[PPT](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2FIndirasribhashyam%2FBanking-Application-with-TCP-Based-Communication-for-Financial-Transactions%2Frefs%2Fheads%2Fmain%2Fnetworks.pptx&wdOrigin=BROWSELINK)

