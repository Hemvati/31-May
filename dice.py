from random import randint

dice=randint(1,6)
guess=int(input("Guess a number:"))

if (guess==dice):
	print("Wohoo you got lucky")
else:
	print("Oops! Better luck next time. Your number was %d",dice)
