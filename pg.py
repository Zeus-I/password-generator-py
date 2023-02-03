import random
import colorama
from colorama import Fore
print(Fore.MAGENTA+"\n<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>")
print("\n           Welcome to FLX Password Generator\n")
print("<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>\n")
ty = int(input(Fore.BLUE+"Enter 1 for quick password and 2 for custom password\n"))
if ty == 2:
  letters = input("\nHow many letters would you like in your password? \n")
  symbols = input("\nHow many symbols would you like in your password? \n")
  numbers = input("\nHow many numbers would you like in your password? \n")  
  ad = int(letters)
  bd = int(symbols)
  cd = int(numbers)
elif ty == 1:
  ad = random.randint(3,6)
  bd = random.randint(2,5)
  cd = random.randint(3,5)
else:
  print("Enter 1 or 2 only")

al= "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
sy= "~ ! @ # $ % ^ & * ( ) _ - + = { } [ ] | \ ; : < , > . ? / `"
nu= "1 2 3 4 5 6 7 8 9 0"

alpha = al.split()
symb = sy.split()
numb = nu.split()
passx=""
password = []
for i in range(1,ad+1):
  i = random.choice(alpha)
  password.append(i)
for j in range(1,bd+1):
  j = random.choice(symb)
  password.append(j)
for k in range(1,cd+1):
  k = random.choice(numb)
  password.append(k)
random.shuffle(password)
det= len(password)

for nt in range(det):
  passx = str(password[nt]) + passx
print(Fore.YELLOW+f'''            __________________________________________________
           |    _________________________________________     |
           |   |                                         |    |
           |   |  C:\> _ password generated              |    |
           |   |                                         |    |
           |   |                {passx}                  |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |_________________________________________|    |
           |                                                  |
            \_________________________________________________/
                   \___________________________________/
                ___________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
:-------------------------------------------------------------------------:
`---._.-------------------------------------------------------------._.---'
''')
print(Fore.WHITE+f"")