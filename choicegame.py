print("Welcome to the game of horrors")

avatar = input("Who are you? ")

print("You are all alone in a distant island and you come across three caves... which one would you choose? (Type response - one, two, three)")
cave = input("Which cave? ")

if cave == "one":
    print("Game Over")
elif cave == "two":
    print("The cave of destiny.. you have come across a treasure chest and weapon chest.. what would you pick?..\n Remember saving yourself and getting out of the island is your first priority")
    choice1 = input("So what do you pick? Treasure or Weapon: ")
    if choice1 == "treasure":
        print("Game Over")
    elif choice1 == "weapon":
        print("Good Job you just defeated the Chrispel of the dead jungle")
        print("Here is your reward 💰... do you wish to claim it or get out of the island?")
        print("(Y) for Claim and (N) for getting out of the island")
        final_choice1 = input().lower()
        if final_choice1 == "y":
            print("Game Over")
        elif final_choice1 == "n":
            print("Thank you for playing")
            print("You have successfully completed the game and have also won the reward... Since you chose..\n since you chose morality over greed")
            print(f"{avatar} YOu are the Saviour of Jumanji")
        else:
            print("Invalid input. Please try again.")
    else:
        print("Invalid input. Please try again.")
elif cave == "three":
    print("You come across 3 bottles of potion with a note that says\n Whoever wil; drink this can fly or live forever or you can summon a genie")
    print("What would you choose? a, for flying, b, immortality and c, for genie")
    choice2 = input().lower()
    if choice2 == "a":
        print("Congratulations, you have completed the game and successfully won the reward.. and got out of the island")
        print("You must be on cloud nine!!")
        print(f"{avatar} You are a very lucky person, i must say!!!")
    elif choice2 == "b":
        print("Some island locals found you and tried to torture you to death\n but oh no.. you're now just tortured for eternity!!")
        print(f"{avatar}! Game over")
    elif choice2 == "c":
        print("Genies dont exist.. and why the hell would a genie ever help you?")
        print("Game over")
    else:
        print("Invalid input. Please try again.")
else:
    print("Invalid input. Please try again.")