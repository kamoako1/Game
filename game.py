from random import randint

def rpsGame():
    print("Welcome to the Rock, Paper, Scissors Game!")
    choices = ["Rock", "Paper", "Scissors"]

    agent = choices[randint(0,2)]
    answer = int(input("How many rounds would you like to play?  "))

    while answer > 0:
    
        user = input("Rock, Paper, Scissors? (Enter first letter as Uppercase)  ")
        if user == agent:
                print("Agent chose", agent)
                print("Tie!")
        elif user == "Paper":
                if agent == "Rock":
                    print("Agent chose", agent)
                    print("You win!", user, "covers", agent)
                else:
                    print("Agent chose", agent)
                    print("You lose!", agent, "cut", user)
        elif user == "Rock":
                if agent == "Scissors":
                    print("Agent chose", agent)
                    print("You win!", user, "breaks", agent)
                else:
                    print("Agent chose", agent)
                    print("You lose!", agent, "covers", user)
        elif user == "Scissors":
                if agent == "Paper":
                    print("Agent chose", agent)
                    print("You win!", user, "cuts", agent)
                else:
                    print("Agent chose", agent)
                    print("You lose!", agent, "breaks", user)
        else:
                    print("Invalid input. Try again!")
        agent = choices[randint(0,2)]
        answer -= 1
    replay = input("Thanks for playing! Would you like to play again? (Enter 'yes' for yes Enter any key for no) ")
    while True:
    
        if replay == 'yes':
            True
            rpsGame()
        else:
            print("Game closed. Thanks for playing. See you later!")
            False
            repeat='no'
            answer=0
            break
        return
            
rpsGame()