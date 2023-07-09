from os import system,name
from time import sleep
 
system('cls' if name=='nt' else 'clear')


system('rm -rf main.py')
sleep(0.1)
system('wget https://raw.githubusercontent.com/Retnox/main.py')
print(r+"└─ "+w+"\033[1;37m>>> Script Updated <<<")
sleep(0.5)

#system('python main.py' if name=='nt' else 'python3 main.py')
print('script updated now run the script again')
