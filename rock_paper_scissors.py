player1 = input("Player 1, enter rock, paper, or scissors: ")
player2 = input("Player 2, enter rock, paper, or scissors: ")

if player1 == player2:
    print("The game is a tie.")

elif (player1 == "rock" and player2 == "scissors") or \
     (player1 == "scissors" and player2 == "paper") or \
     (player1 == "paper" and player2 == "rock"):
    print("Player 1 wins!")

elif (player2 == "rock" and player1 == "scissors") or \
     (player2 == "scissors" and player1 == "paper") or \
     (player2 == "paper" and player1 == "rock"):
    print("Player 2 wins!")

else:
    print("Invalid choice.")
