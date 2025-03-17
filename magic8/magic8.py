import random # to generate random numbers for index

name = "Matthew" # Name used in program

question = "Will this program be awesome?" # Question to ask to magic8 ball

answer = "" # Empty string representing the default answer before it is assigned to a value from the below phrases array

phrases = ["Yes - definitely", "It is decidedly so", "Without a doubt", "Reply hazy, try again", "Ask again later", "Better not tell you now", "My sources say no", "Outlook not so good", "Very doubtful"] # An array of the 9 possible phrases that the magic8 ball can say
random_number = random.randint(1, 9) # imported from "random" to create a random number between 1 and 9

print(random_number)


if random_number == 1:
    print("Yes - Definitely")
else:
    print("NOPE!")


