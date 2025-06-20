print("Name: Siddharth A Gurav")
print("USN: 1AY24AI107")
print("Section: O")

import random

def play():
    user = input("Choose 'rock', 'paper' or 'scissors': ").lower()
    computer = random.choice(['rock', 'paper', 'scissors'])

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        return "It's a tie!"
    
   
    if is_win(user, computer):
        return "You win!"
    
    return "You lose!"

def is_win(player, opponent):
    
    return (player == 'rock' and opponent == 'scissors') or \
           (player == 'scissors' and opponent == 'paper') or \
           (player == 'paper' and opponent == 'rock')


while True:
    print("\n--- Rock Paper Scissors ---")
    result = play()
    print(result)
    
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
