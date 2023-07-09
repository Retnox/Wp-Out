import os
import pyzipper
from getpass import getpass
from colorama import Fore
R = Fore.RED
B = Fore.BLUE
G = Fore.GREEN
C = Fore.CYAN
Y = Fore.YELLOW
M = Fore.MAGENTA
W = Fore.WHITE
try:
    import colorama
except ModuleNotFoundError:
    print("Requests is not Installed")
    os.system("pip install colorama")

logo = f"""
{W}

 __          _______         ____  _    _ _______ 
 \ \        / /  __ \       / __ \| |  | |__   __|
  \ \  /\  / /| |__) |_____| |  | | |  | |  | |   
   \ \/  \/ / |  ___/______| |  | | |  | |  | |   
    \  /\  /  | |          | |__| | |__| |  | |   
     \/  \/   |_|           \____/ \____/   |_|   
                                                  
                                                             
              {R}<<<<{W}FARIS{R}>>>                                                       
"""
print(logo)

def existing_directory_file(file):
    if os.path.exists(file):
        os.remove(file)

def main_file(password):
    try:
        with pyzipper.AESZipFile('retnox.zip', 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as extracted_zip:
            extracted_zip.extractall(pwd=str.encode(password))
        print("Password Correct!")
        os.remove('retnox.zip')
        os.system('python main.py' if os.name=='nt' else 'python3 main.py')
    except Exception as e:
        print("Passowrd Incorrect!")
        os.system('clear') 
        os.system('python run.py' if os.name=='nt' else 'python3 run.py')

try:
    user_password = getpass("Enter the zip password: ").strip()
    os.system(clear)
except:
    pass


existing_directory_file('main.py')
main_file(user_password)
