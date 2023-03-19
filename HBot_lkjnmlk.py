import os

if os.geteuid() != 0:
    Write.Print("This program must be run with (root) privileges!",Colors.orange,interval=0.00)
    exit(1)

# The rest of your code goes here...


import socket
import datetime
import os
import time
from pystyle import *
os.system("clear")
Write.Print("""                                                                  
   _________
  < lkjnmlk >
   ---------
          \   ^__^
           \  (oo)\_______
              (__)\       )\/\
                  \n                  ||----w |
                  ||     ||



""",Colors.red_to_yellow,interval=0.01)
print(Box.DoubleCube("""Telegram  :   @TSL1HACK
Instagram :   hl1.k
"""))
Write.Print("""
1. 22 > SSH
2. 23 > TELENET


""",Colors.green_to_red,interval=0.00)
port_choice = Write.Input("Please choose a port : ",Colors.green_to_red,interval=0.00)
message = Write.Input("Please enter a message for the attacker : ",Colors.green_to_red,interval=0.00)

if port_choice == '2':
    PORT = 23
elif port_choice == '1':
    PORT = 22
else:
    Write.Print("Invalid choice. Exiting...\n\n",Colors.orange,interval=0.00)
    exit()

HOST = ''
file_num = 1
filename = f'captured_data_{file_num}.txt'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    Write.Print("_____________________________________________",Colors.orange,interval=0.00)
    Write.Print(f'\nListening on port {PORT}...\n',Colors.white_to_red,interval=0.00)
    with open(filename, 'a') as f:
        while True:
            conn, addr = s.accept()
            with conn:
                Write.Print(f'\nConnection from {addr} established.',Colors.green,interval=0.00)
                conn.sendall(message.encode())
                while True:
                    try:
                        data = conn.recv(1024).decode('ISO-8859-1')
                        if not data:
                            break
                        Write.Print(f'\nReceived: {data}',Colors.green,interval=0.00)
                        f.write(data)
                    except ConnectionResetError:
                        break
                Write.Print("\n____________________________________________",Colors.green,interval=0.00)
                now = datetime.datetime.now()
                f.write(f"\nData captured on {now.strftime('%Y-%m-%d %H:%M:%S')} from {addr}\n")
                
            file_size = os.stat(filename).st_size
            # If file size exceeds 10MB, start writing to a new file
            if file_size > 10485760:
                file_num += 1
                filename = f'captured_data_{file_num}.txt'
                with open(filename, 'a') as f:
                    Write.Print(f"\nNew file created: {filename}",Colors.green,interval=0.00)
                    now = datetime.datetime.now()
                    f.write(f"\nNew file created on {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
