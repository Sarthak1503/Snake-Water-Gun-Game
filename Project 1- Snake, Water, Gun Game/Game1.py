import random

#Snake Water Gun or Rock Paper Scissors
def gameWin(comp, you):


    #if two values are equal, declare a tie!
    if comp == you:
        return None
    #check for all possibilities when computer chose s
    elif comp =='s':
        if you =='w':
            return False
        elif you =='g':
            return True
    #check for all possibilities when computer chose s
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    #check for all possibilities when computer chose s
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

name = input("\nEnter your name here: ")
print("\nComp Turn: Snake(s) Water(w) Gun(g)? ") 
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
you = input(f"\n{name}'s Turn: Snake(s) Water(w) Gun(g)? ") 
a= gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"{name} chose {you}")


if a == None:
    print("\nThe game is a tie!")
elif a == True:
    print("\nYou win!")
else:
    print("\nYou lose!")
