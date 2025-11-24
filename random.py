import random

def main():
    print("--- Number Guessing Game ---")
    # Generate a random number between 1 and 100
    secret = random.randint(1, 100)
    guess = None
    attempts = 0

    print("I have selected a number between 1 and 100. Can you guess it?")

    # Loop until the user guesses correctly
    while guess != secret:
        try:
            # Get input from user
            user_input = input("Enter your guess: ")
            guess = int(user_input)
            attempts += 1

            # Check conditions
            if guess < secret:
                print("Too low! Try again.")
            elif guess > secret:
                print("Too high! Try again.")
            else:
                print(f"Correct! You won in {attempts} attempts.")
                print(f"The number was indeed {secret}.")
        
        except ValueError:
            # Handle non-numeric inputs
            print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()