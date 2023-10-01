import random

computerScore = 0
yourScore = 0


def display_score():
    print("                Score               ")
    print("-" * 35)
    print("|       You      |    Computer    |")
    print("|{: ^16}|{:^16}|".format(yourScore, computerScore))
    print("-" * 35)


def display_choice(you, computer):
    print("  You   :", full_name(you))
    print("Computer:", full_name(computer))


def computer_random_choice():
    return random.choice(['r', 'p', 's'])


def full_name(opt):
    names = {'r': "Rock", 'p': "Paper", "s": "Scissor"}
    return names[opt]


def play_game():
    global computerScore, yourScore
    you = input("\n\nRock|Paper|Scissor (R|P|S) : ").lower()

    if you not in "rps":
        print("Invalid Input")
        return

    comp = computer_random_choice()

    if you == comp:
        print("\n         ^ Tie ^")
    elif (you == 'r' and comp == 's') or (you == 's' and comp == 'p') or (you == 'p' and comp == 'r'):
        print("\n      *** You Won ***")
        yourScore += 1
    else:
        print("\n      +++ You lost +++")
        computerScore += 1

    display_choice(you, comp)
    display_score()


while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print("Thanks for playing!")
