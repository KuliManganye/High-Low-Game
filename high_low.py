import random
from high_low_doc import data
from high_low_art import logo
from high_low_art import vs
import os

# Generate a random account from the game data. Given our document this function will always choose a random account to compare against
def shuffled_data():
    return random.choice(data)


# Format the account data into printable format
def account_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    #print(f"{name}, a {description}, from {country}")
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess and returns True if they got it right. Or False if they got it wrong"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    # The score variable is to keep count of how many the user has gotten correct so far. If the user gets one answer wrong. The game ends and resets back to the start
    score = 0
    # This is to allow a while loop to loop the game till the player gets an answer wrong
    continue_game = True
    # Assign the values to be compared to the shuffle function that will ensure it picks out one account randomly each time to assign to the variable
    account_a = shuffled_data()
    account_b = shuffled_data()

    while continue_game:
        account_a = account_b
        account_b = shuffled_data()

        # Each time the user gets the guess correctly, the account that previously made up B will now be moved to A and a new random account selected to be assigned to B
        while account_a == account_b:
            account_b = shuffled_data()

        # This is what will be printed before each round
        print(f"Compare A: {account_data(account_a)}.")
        print(vs)
        print(f"Against B: {account_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        # The value to be compared each time is the follower_count. So assign the compare variables to the follower_count key in the dictionary and it will compare the values of the key
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        """Call the check answer function that checks if the follower_count at account A is higher than the follower_count at account B. And return A if it is higher than B or B if B is 
        higher than A"""
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        # Clear the terminal after each round
        os.system("cls")
        # Print the game logo at the start of the game
        print(logo)

        if is_correct:
            # Add 1 to the user's score each time they get the answer correctly.
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            # End the game each time the user gets the answer wrong
            continue_game = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()