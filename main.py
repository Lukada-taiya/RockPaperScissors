# STUDENT ID: 20200404058
# CSC MINI PROJECT ASSIGNMENT

import random

# This list shows what option can beat what option. Eg, rock beats scissors
WIN_LIST = [('ROCK', 'SCISSORS'),
            ('SCISSORS', 'PAPER'),
            ('PAPER', 'ROCK')]
#  list of selections
SELECTIONS_LIST = ['ROCK', 'PAPER', 'SCISSORS']

#  This dictionary keeps track of the wins of both player and computer, and ties
stats_count = {'player': 0, 'computer': 0, 'ties': 0}


# Main menu for the Game
def welcome():
    while True:
        option = input(
            "\n\n======== ROCK PAPER SCISSORS GAME ======="
            "\n\n1. Play\n2. Exit\n")
        if option == '1':
            play_game()
        elif option == '2':
            print("Thank you for playing my game.")
            exit()
        else:  # if there's an invalid option, the menu will start again
            print("Invalid option. Try again...\n")


# Game function
def play_game():
    instructions = (" Instructions "
                    "\n You can choose either Rock, Paper or Scissors. Keep in mind that: "
                    "\n * Rock crushes Scissors"
                    "\n * Scissors cuts Paper"
                    "\n * Paper covers Rock"
                    "\n Meaning, if you choose Rock but your opponents chooses Scissors, you win. The same goes for "
                    "the rest. "
                    "\nThe first person to score 5 points WINS the game!"
                    "\nIf you want to go over the rules, just type 'help'."
                    "\nIf you want to end the game, type 'quit'.\nGOOD LUCK\n")
    print(instructions)

    while True:
        player_selection = input("Enter your Choice {}: ".format(SELECTIONS_LIST))
        player_selection = player_selection.upper()

        if player_selection in SELECTIONS_LIST:
            computer_selection = random.choice(SELECTIONS_LIST)

            print("Player Selection: {}".format(player_selection))
            print("Computer Selection: {}".format(computer_selection))

            match = player_selection, computer_selection  # converts the player's and computer's selection into a
            # tuple to compare it to WIN_LIST

            if player_selection == computer_selection:  # if both selections (player and computer) are the same,
                # a tie count is added to the dictionary
                stats_count['ties'] += 1
                print("\nResult: Both are {}! So it's a Tie!".format(player_selection))
            elif match in WIN_LIST:  # if the tuple is the same as the WIN_LIST, player wins and a player count is
                # added to the dictionary
                stats_count['player'] += 1
                print("\nResult: {} beats {}! You won!".format(player_selection, computer_selection))
            else:  # if none of the conditions above are true, computer wins and a computer count is added to the
                # dictionary
                stats_count['computer'] += 1
                print("\nResult: {} beats {}! You lost!".format(computer_selection, player_selection))
            print("-------  SCOREBOARD  -------"
                  "\n YOU  | COMPUTER | DRAW"
                  "\n  {player}        {computer}        {ties}"
                  "\n-----------------------".format(**stats_count))
            if stats_count['player'] == 5:  # if player gets 5 points, he wins
                print("The game is DONE! You won! Congratulations!")
                break
            elif stats_count['computer'] == 5:  # if computer gets 5 points, it wins
                print("The game is DONE! You lost. Better luck next time.")
                break
        elif player_selection == 'HELP':  # if the user doesn't remember the rules, it will show them again
            print(instructions)
        elif player_selection == 'QUIT':  # if the user wants to quit the game, it will take him to main menu
            stats_count['player'] = 0
            stats_count['computer'] = 0
            stats_count['ties'] = 0
            input("You are a quitter! Shame on you! Please press ENTER to continue...")
            break
        else:
            print("Invalid selection. Try again...")  # if there's an invalid choice, the input will show again


#  beginning of program
welcome()
