import random

computerScore = 0
yourScore = 0


def displayScore():
    print("                Score               ")
    print("-"*35)
    print("|       You      |    Computer    |")
    print("|{: ^16}|{:^16}|".format(yourScore, computerScore))
    print("-"*35)


def displayChoice(you, computer):
    print("  You   :", fullName(you))
    print("Computer:", fullName(computer))


def computerRand():
    return random.choice(['r', 'p', 's'])


def fullName(opt):
    names = {'r': "Rock", 'p': "Paper", "s": "Scissor"}
    return names[opt]


def game():
    global computerScore, yourScore
    you = input("\n\nRock|Paper|Scissor (R|P|S) : ").lower()
    if you not in "rps":
        print("Invalid Input")
        return
    comp = computerRand()
    if you == comp:
        print("\n         ^ Tie ^")
    elif (you == 'r' and comp == 's') or (you == 's' and comp == 'p') or (you == 'p' and comp == 'r'):
        print("\n      *** You Won ***")
        yourScore += 1
    else:
        print("\n      +++ You lost +++")
        computerScore += 1
    displayChoice(you, comp)
    displayScore()


while True:
    game()
