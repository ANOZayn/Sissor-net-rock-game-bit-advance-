import random
print("!!!A SIMPLE ROCK SISSORS AND NET GAME!!!")
guess_count = 0
win = 0
# invalid = 0
guess_limit = 3
out_of_guesses = False
while not(out_of_guesses):
    if guess_count < guess_limit:
      move = input("Enter your move:")
      comp = random.choice(["rock", "net", "sissor"])
      print(comp)
      if move == comp:
           print("Draw")
           guess_count += 1
      elif comp != "rock" and comp != "net" and move == "rock":
           print("You won!!!")
           win += 1
           guess_count += 1
      elif comp != "net" and comp != "sissor" and move == "net":
            print("You win!!!")
            win += 1
            guess_count += 1
      elif comp != "rock" and comp != "sissor" and move == "sissor":
            print("You won!!!")
            win += 1
            guess_count += 1
      elif comp != "rock" and comp != "sissor" and move == "rock":
            print("You lose!!!")
            win -= 1
            guess_count += 1
      elif comp != "net" and comp != "sissor" and move == "sissor":
            print("You lose!!!")
            win -= 1
            guess_count += 1
      elif comp != "rock" and comp != "net" and move == "net":
            print("You lose!!!")
            win -= 1
            guess_count += 1
      elif move!="rock" and move!="net" and move!="sissor" :
          print("Invalid move")
          guess_count += 1
          # invalid += 1

    else:
        out_of_guesses = True
           # guess_count += 1
if out_of_guesses:
    if win > 0 and invalid:
        print("You win")
    # print("Out of guesses, You Lose!")
    elif win == 0:
        print("Draw bhayo")
    else:
        print("Hariyo naramrari")
# else:
 #   print("")
