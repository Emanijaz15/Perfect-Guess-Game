import random
num=random.randint(1,100)
guess=0
while True:
        guess+=1
        user=int(input("Guess the number: "))
        if user == num:
            print("Congrats!! You guessed it!!")
            print(f"your guesses are {guess}")
            break
        elif user < num:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

