import random
num=random.randint(1,100)
while True:
        user=int(input("Guess the number: "))
        if user == num:
            print("Congrats!! You guessed it!!")
            break
        elif user < num:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")


