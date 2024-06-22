#Quiz_Game...

import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

print(Fore.MAGENTA + Style.BRIGHT + "Welcome to Science Parliament Quiz. ")
print(Fore.LIGHTMAGENTA_EX + Style.DIM + "Let's see how well you know your government agencies!")

print()
playing  = input(Fore.CYAN+ Style.BRIGHT + "Do you want to play(yes/no) ? ")

if playing.lower() != "yes":
    quit() #to quit the code if answer is other than yes

print(Fore.LIGHTCYAN_EX + "Okay! Let's play :) ")
score = 0

print()
ans = input(Fore.BLACK + Style.BRIGHT + "1.What does DRDO stand for? ")
if ans.lower() == "defence research and development organisation":
    print(Fore.BLUE + "Correct")
    score += 1
else:
    print(Fore.RED + "Incorrect")

print()
ans = input(Fore.BLACK + Style.BRIGHT + "2.What does ISRO stand for? ")
if ans.lower() == "indian space research organisation":
    print(Fore.BLUE + "Correct")
    score += 1
else:
    print(Fore.RED + "Incorrect")

print()
ans = input(Fore.BLACK + Style.BRIGHT + "3.What does MST stand for? ")
if ans.lower() == "ministry of science and technology":
    print(Fore.BLUE + "Correct")
    score += 1
else:
    print(Fore.RED + "Incorrect")

print()
ans = input(Fore.BLACK + Style.BRIGHT + "4.What does DOS stand for? ")
if ans.lower() == "department of space":
    print(Fore.BLUE + "Correct")
    score += 1
else:
    print(Fore.RED + "Incorrect")

print()
ans = input(Fore.BLACK + Style.BRIGHT + "5.What does ICMR stand for? ")
if ans.lower() == "indian council of medical research":
    print(Fore.BLUE + "Correct")
    score += 1
else:
    print(Fore.RED + "Incorrect")

print()
ans = input(Fore.BLACK + Style.BRIGHT + "6.What does MEITY stand for? ")
if ans.lower() == "ministry of electronics & information technology":
    print(Fore.BLUE + "Correct")
    score += 1
else:
    print(Fore.RED + "Incorrect")

print()
ans = input(Fore.BLACK + Style.BRIGHT + "7.What does MOES stand for? ")
if ans.lower() == "ministry of earth sciences":
    print(Fore.BLUE + "Correct")
    score += 1
else:
    print(Fore.RED + "Incorrect")

print()
print("You got " +  str(score) + " Questions correct!")
print("You got " + str((score / 7)*100) + "%")
