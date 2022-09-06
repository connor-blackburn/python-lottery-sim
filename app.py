''' 
A simulated lottery experience with numbers from 0-20. 
A randomly generated winning ticket will be created upon each attempt.
My tickets numbers will remain the same.
A counter will record how many attempts it took to win.
'''

# Will generate a random integer between a given range
from random import randint

# My chosen numbers for my ticket in an array
my_ticket = [13, 1, 3, 14, 20]

# Setting the counter to 0 which will track how many attempts it takes to win the lottery
counter = 0

while(True):

	# Will generate the winning ticket, generating 5 random numbers between 1 an 20
	winning_ticket = [randint(1,20) for x in range(1,6)]

	if (set(my_ticket) == set(winning_ticket)):
		print(f'\nYou win after {counter} attempts!')
		counter = 0
		print(f"counter reset - {counter}")
		break
	else:
		# If we didnt win, increment counter by 1 and generate a new winning ticket to check against mine
		counter += 1
		winning_ticket = [randint(1,20) for x in range(1,6)]
		print(winning_ticket)
		print(counter)
