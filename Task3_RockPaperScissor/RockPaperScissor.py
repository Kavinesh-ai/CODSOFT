import random

print(" Welcome to Rock, Paper, Scissors!")
u_score = 0
c_score = 0

while True:
    
    u_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    if u_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please enter rock, paper, or scissors.\n")
        continue

    c_choice = random.choice(["rock", "paper", "scissors"])

    print(" Your Score: ",u_score)
    print(" Computer Score: ",c_score)

    if u_choice == c_choice:
        print(" It's a Tie!")

    elif (
        (u_choice == "rock" and c_choice == "scissors") or
        (u_choice == "paper" and c_choice == "rock") or
        (u_choice == "scissors" and c_choice == "paper")
    ):
        print("You Win!")
        u_score += 1

    else:
        print("You Lose!")
        c_score += 1

    # Display Scores
    print("\nScoreboard")
    print(" Your Score: ",u_score)
    print(" Computer Score: ",c_score)

    play_again = input("\nPlay again? (yes/no): ").lower()

    if play_again != "yes":
        print("\n Final Scores")
        print(" Your Score: ",u_score)
        print(" Computer Score: ",c_score)
        print("Thanks for playing!")
        break

    print("\n" + "-" * 40 + "\n")
