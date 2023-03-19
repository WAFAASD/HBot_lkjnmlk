# Simple Server for Listening on Port SSH or TELNET

This code can be used to create a simple server for listening on either SSH or TELNET port and capturing the data sent to the server.

## Getting Started

### Prerequisites

- Python 3.x
- pystyle library

### Usage

1. Clone this repository.
2. Navigate to the cloned directory in your terminal.
3. Run the following command to install the required library:

pip install pystyle

4. Run the following command to start the server:

python server.py

5. Choose either port 22 (SSH) or port 23 (TELNET) when prompted.
6. Enter a message for the attacker when prompted.
7. The captured data will be stored in a file named "captured_data_X.txt", where X is the file number (e.g., captured_data_1.txt, captured_data_2.txt, etc.).
8. If the file size exceeds 10MB, a new file will be created to store the captured data.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

