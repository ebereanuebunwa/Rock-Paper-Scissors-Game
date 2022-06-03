import random

print("Rock Paper Scissors Game".center(30, '-'))
print("""   Game Rules:
    1. Rock beats Scissors 
    2. Paper beats Rock
    3. Scissors beats Paper
""")
user_name = input("Enter Username: ")
is_running = True

while is_running:
    list_of_plays = ['R', 'P', 'S']
    dict_of_plays = {
        'R': 'Rock',
        'P': 'Paper',
        'S': 'Scissors'
    }

    # User makes makes their choice.
    user_choice = input("Pick your play [Rock(R), Paper(P), Scissors(S)]: ").upper()
    if user_choice not in list_of_plays:
        print("Invalid play!")
        continue
    
    # Computer makes a choice.
    computer_choice = random.choice(list_of_plays)

    # Print plays.
    print(f'Plays: {user_name} ({dict_of_plays[user_choice]}) : CPU ({dict_of_plays[computer_choice]})')

    # Game rules:
    # Rock beats scissors, paper beats rock, scissors beat paper
    if (user_choice == 'R' and computer_choice == 'S') or (user_choice == 'P' and computer_choice == 'R') or \
            (user_choice == 'S' and computer_choice == 'P'):
        print("You win!")
        break

    elif user_choice == computer_choice:
        print("It's a tie.\n\n" + "Reset".center(20, '-'))
        continue

    else:  # Computer wins
        print("Computer wins!")
        break


