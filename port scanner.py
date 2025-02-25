import socket
import sys
import threading
import pyfiglet
from termcolor import colored

#get add a bannner use pyfiglet
banner  = pyfiglet.figlet_format ("port scanner")
colored_banner  = colored(banner, color="green")
print(colored_banner)

print('\n> port scanner\n' + '=' * 15 + '\n')

# Get target IP address
if len(sys.argv) > 1:
    target = socket.gethostbyname(sys.argv[1])
else:
    target = socket.gethostbyname(input('> Enter target: '))

# Function to scan a single port
def scanport(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Set a timeout for the connection
        result = s.connect_ex((target, port))  # Returns 0 if the port is open
        if result == 0:
            print(f' {target} ~ port {port} [open]')
        s.close()
    except Exception as e:
        print(f'Error scanning port {port}: {e}')

# Scan ports 1 to 1024 using threads
for i in range(1, 1025):
    scan = threading.Thread(target=scanport, args=(target, i))
    scan.start()