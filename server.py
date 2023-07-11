#Encrypted by retnox
from colorama import Fore, Style
R = Fore.RED
B = Fore.BLUE
G = Fore.GREEN
C = Fore.CYAN
Y = Fore.YELLOW
M = Fore.MAGENTA
W = Fore.WHITE
# Logo
logo =F"""
{G}

░██████╗███████╗██████╗░██╗░░░██╗███████╗██████╗░
██╔════╝██╔════╝██╔══██╗██║░░░██║██╔════╝██╔══██╗
╚█████╗░█████╗░░██████╔╝╚██╗░██╔╝█████╗░░██████╔╝
░╚═══██╗██╔══╝░░██╔══██╗░╚████╔╝░██╔══╝░░██╔══██╗
██████╔╝███████╗██║░░██║░░╚██╔╝░░███████╗██║░░██║
╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
           
"""


# Server status
server_connected = True

def check_server_status():
    global server_connected
   
    server_connected = False

def display_server_status():
    if server_connected:
     print(f"{R}└─{W}Server is connected.")
    else:
        print(R)
        print("Server is not connected.")

def reconnect_server():
    global server_connected
    print("Attempting to reconnect to the server...")
    
    server_connected = True
    print("Server reconnected successfully.")

if __name__ == "__main__":
    print(logo)
    display_server_status()

    if not server_connected:
        choice = input("└─>Server is not connected. Do you want to reconnect? (y/n): ")
        if choice.lower() == "y":
            reconnect_server()
            display_server_status()
