import random

def number_guessing_game():
    print(" Welcome to Number Guessing Game!")
    print("I will choose a number between 1 and 100.")
    
    
    secret_number = random.randint(1, 100)
    
    attempts = 0
    max_attempts = 7  
    
    print(f"You have {max_attempts} attempts to guess it.\n")
    
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print(" Too low!\n")
            elif guess > secret_number:
                print(" Too high!\n")
            else:
                print(f" Correct! You guessed it in {attempts} attempts.")
                break
                
        except ValueError:
            print(" Please enter a valid number.\n")
    
    else:
        print(f" Game Over! The number was {secret_number}.")

number_guessing_game()