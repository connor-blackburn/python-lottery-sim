''' 
A simulated lottery experience with numbers from 0-20. 
A randomly generated winning ticket will be created upon each attempt.
My tickets numbers will remain the same.
A counter will record how many attempts it took to win.
'''

# Will generate a random integer between a given range
from random import randint
# Will allow me to produce visualisations from my results
import matplotlib.pyplot as plt

# My chosen numbers for my ticket in an array
my_ticket = [13, 1, 3, 14, 20]

# Setting the counter to 0 which will track how many attempts it takes to win the lottery
counter = 0
attempts_array = []

while(len(attempts_array) != 10):

	# Will generate the winning ticket, generating 5 random integers between 1 an 20
	winning_ticket = [randint(1,20) for x in range(1,6)]

	# conditional statement to check if both tickets match, if they do, display how many attempts it took and reset the counter
	if (set(my_ticket) == set(winning_ticket)):
		print(f'\nYou win after {counter} attempts!')
		attempts_array.append(counter)
		counter = 0
		print(f"counter reset - {counter}")
	else:
		# If we didnt win, increment counter by 1 and generate a new winning ticket to check against mine
		counter += 1
		winning_ticket = [randint(1,20) for x in range(1,6)]
		print(winning_ticket)
		print(counter)

print(attempts_array)


# Generating the visualisation
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.style.use('seaborn-darkgrid')

fig, ax = plt.subplots(figsize=(12,8))

plt.plot(x, attempts_array, marker='o')

plt.xlabel('Number of Wins', size=12)

plt.ylabel('Attempts', size=12)

plt.title("Number of attempts to win the lottery")

for index in range(len(x)):
  ax.text(x[index]+.1, attempts_array[index], attempts_array[index], size=10)

plt.tight_layout()

plt.show()
