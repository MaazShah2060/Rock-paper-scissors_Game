import random
r = 'rock'
p = 'paper'
s = 'scissors'
x = '1'
while x=='1':
    choice = input("enter your choice r,p,s: ")
    comp_choice = random.randrange(0,3)
    if(choice=='r'):
        print("Your choice: ",r)
        if(comp_choice==0):
            print("Computer's choice: ",r)
            print('***Draw -_-***')
        elif(comp_choice==1):
            print("Computer's choice: ", p)
            print('***You lose :(***')
        else:
            print("Computer's choice: ", s)
            print('***You win :)***')
    if(choice=='p'):
        print("Your choice: ", p)
        if(comp_choice==0):
            print("Computer's choice: ", r)
            print('***You win :)***')
        elif(comp_choice==1):
            print("Computer's choice: ", p)
            print('***Draw -_-***')
        else:
            print("Computer's choice: ", s)
            print('***You lose :(***')
    if(choice=='s'):
        print("Your choice: ", s)
        if(comp_choice==0):
            print("Computer's choice: ", r)
            print('***You lose :(***')
        elif(comp_choice==1):
            print("Computer's choice: ", p)
            print('***You win :)***')
        else:
            print("Computer's choice: ", s)
            print('***Draw -_-***')
    x = input("Press 1 to play again or any other key to exit: ")
