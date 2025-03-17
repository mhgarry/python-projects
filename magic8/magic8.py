import random # to generate random numbers for index
from email.policy import default

name = "" # Name used in program

question = "Will this be a good program?" # Question to ask to magic8 ball

answer = "" # Empty string representing the default answer before it is assigned to a value from the below phrases array

phrases = ["Yes - definitely", "It is decidedly so", "Without a doubt", "Reply hazy, try again", "Ask again later", "Better not tell you now", "My sources say no", "Outlook not so good", "Very doubtful", "Ehhhh....idk", "Maybe in another lifetime", "Non-zero", "Nahhh"] # An array of the 9 possible phrases that the magic8 ball can say

random_number = random.randint(1, 12) # imported from "random" to create a random number between 1 and 9


if random_number == 1:
    answer = phrases[0]
elif random_number == 2:
    answer = phrases[1]
elif random_number == 3:
    answer = phrases[2]
elif random_number == 4:
    answer = phrases[3]
elif random_number == 5:
    answer = phrases[4]
elif random_number == 6:
    answer = phrases[5]
elif random_number == 7:
    answer = phrases[6]
elif random_number == 8:
    answer = phrases[7]
elif random_number == 9:
    answer = phrases[8]
elif random_number == 10:
    answer = phrases[9]
elif random_number == 11:
    answer = phrases[10]
elif random_number == 12:
    answer = phrases[11]
else:
    print("Error.")


if not question:
  print("Please enter a valid question.")
elif not name:
  print("Magic 8-Ball's answer: ", [answer])

else:
  print(f"{name} asks: ", [question])
  print("\n")
  print("Magic 8-Ball's answer: ", [answer])