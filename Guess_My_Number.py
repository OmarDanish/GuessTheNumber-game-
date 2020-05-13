print ("      ")
\
import random 

x=int(input("\nThe computer will choose a number from 1-x, what do you want x to be?\n"))

number=random.randrange(1,x)

user_guess=int(input("\nGuess a number between 1 and {}\n".format(x)))

while user_guess != number:
    if user_guess < number:
        print ('\nThats too low, guess higher\n')
        user_guess=int(input(""))
    else:
        print ('\nThats too high, guess lower\n')
        user_guess=int(input(""))

print ('\nYou guessed the number correctly, you win!')
