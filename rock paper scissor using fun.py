p1action=input()
p2action=input()
def rockpaperscissor():
    if p1action == p2action:
        print("try another time")
    elif p1action == "rock":
        if p2action == "scissor":
            print("congrats p1 on winning the game")
        else:
            print("congrats p2 on winning the game")
    elif p1action == "paper":
        if p2action == "rock":
            print("congrats p1 on winning the game")
        else:
            print("congrats p2 on winning the game")
    elif p1action == "scissor":
        if p2action == "paper":
            print("congrats p1 on winning the game")
        else:
            print("congrats p2 on winning the game")
    p = input("want to play or not")
    if (p == "yes"):
        print("start making actions")
    else:
        print("thank you for playing the game")
rockpaperscissor();
