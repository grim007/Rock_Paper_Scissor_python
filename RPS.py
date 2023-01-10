import random
def gamewin():
    if comp==you:
        return None

    if comp=="s":
        if you=="p":
            return False
        elif you=="r":
            return True

    if comp=="p":
        if you=="r":
            return False
        elif you=="s":
            return True

    if comp=="r":
        if you=="s":
            return False
        elif you=="p":
            return True                
    

print("Computer's turn: Scissor(s), Paper(p) or Rock(r)")
rnd=random.randint(1,3)
if rnd==1:
    comp="s"

elif rnd==2:
    comp="p"

elif rnd==3:
    comp="r"

you=input("Your turn: Scissor(s), Paper(p) or Rock(r) ")
if rnd==1:
    print("The Computer chose Scissors")

elif rnd==2:
    print("The Computer chose Paper")

elif rnd==3:
    print("The Computer chose Rock")

n=gamewin()
if n==True:
    print("Congratulations!!! You won")

elif(n==False):
    print("You lost bozo")
    
elif(n==None):
    print("The game ended in a tie")

