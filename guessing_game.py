import random


def play_game():
    secret_no=random.randint(1,100)
    attempts=0
    print("i am thinking of a number between 1 and 100")
    while True:
        guess=int(input("Take a guess:"))
        attempts=attempts+1
        if guess<  secret_no:
            print("Too low")
        elif guess> secret_no:
            print("Too high")
        else:
            print("yass,you did it")
            break
play_game()
