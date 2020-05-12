print ("      ")
\
import random 

number=random.randrange(1,50)

user_guess=int(input("\nGuess a number between 1 and 50:\n"))

while user_guess != number:
    if user_guess < number:
        print ('\nThats too low, guess higher\n')
        user_guess=int(input(""))
    else:
        print ('\nThats too high, guess lower\n')
        user_guess=int(input(""))

print ('\nYou guessed the number correctly, you win!')