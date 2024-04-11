print(".................M_I_N_D...............G-A-M-E-S................. \n GUESS THE CORRECT NUMBER")
q = input("Tap on the terminal first\n press enter")
print("INSTRUCTIONS/RULES \n 1.) you have to guess the correct number between 0 to 99 \n 2.) if you want to exit the game then type 10 \n 3.) To start the game write your name and press enter")
y = input("If you read the instruction/rules then press enter")
user = input("Enter your name: ")
print("Hello player", user)
print("welcome to the Game \n now game starts to continue")
x = input("press enter")
import random
nump = random.randint(0,99)
# print(nump) if anybody wants to see the answer/number
n = int(input("enter a 2 digit number: "))

while n!=10 :
    num= nump
    cor = 0
    while num%10 :
        numc= num%10
        nc= n%10
        num=num//10
        n=n//10
        if numc==nc :
            cor=cor+1

    if cor==2 :
        print("congrats! you guessed it right \n you are the winner. \n developed by ADITYA KUMAR")
        break
    else :
        print("%d digits were guessed right"%cor)
        n = int(input("enter a 2 digit number: "))
else :
    print("..............--------------you quit the game..............-------------------_________________ \n This game is developed by ADITYA KUMAR")
