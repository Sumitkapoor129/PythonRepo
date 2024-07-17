import random
i=1
while i==1:
    Game=["rock","paper","scissors"]
    CPU= random.choice(Game)
    print("Choose rock, paper or scissors")
    user = input()
    if user=="rock" and CPU=="scissors":    
        print(CPU,"You Won")
    elif user=="paper" and CPU=="rock":    
        print(CPU,"You Won")
    elif user=="scissors" and CPU=="paper":
        print(CPU,"You Won")
    elif user=="scissors" and CPU=="rock":
        print(CPU,"You loose")
    elif user=="rock" and CPU=="paper":
        print(CPU,"You loose")
    elif user=="paper" and CPU=="scissors":
        print(CPU,"You loose")    
    else:
        print(CPU,"Draw",user)              