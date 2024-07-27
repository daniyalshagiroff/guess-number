import random

random_number=random.randint(1, 100)
    
def compare(user_input, random_number):
    if user_input>random_number:
        print("Too high")
        return False
    elif user_input<random_number:
        print("Too low")
        return False
    else:
        print(":-)")
        return True
        
def play_game():
    while True:
        user_input=input("Choose difficulty: easy / hard: ").lower()

        if user_input=="easy":
            attempts=10
            break
        elif user_input=="hard":
            attempts=5
            break
        else:
            print("Incorrect input. Please enter again")
        
    for i in range(0, attempts):
        print(f'You have {attempts-i} attempts remaining to guess a number.')
        guess=int(input("Make a guess: "))
        if compare(guess, random_number)==True:
            print(f"You got it! The answer was {guess}")
            break
        else:
            if i==attempts-1:
                print("You've run out of guesses, you lose.")
            continue
    
play_game()

    
    