import random

name = "" # name of user asking question
question = "Will this be a good program?" # question
phrases = [
    "Yes - definitely", "It is decidedly so", "Without a doubt",
    "Reply hazy, try again", "Ask again later", "Better not tell you now",
    "My sources say no", "Outlook not so good", "Very doubtful",
    "Ehhhh....idk", "Maybe in another lifetime", "Non-zero", "Nahhh"
] # Possible answers

random_number = random.randint(1, len(phrases)) # generate a random index between 1 and length of phrases list
answer = phrases[random_number - 1] # Check index position -1 for the answer the corresponds to the indexed value of the ranom phrase

if not question:
    print("Please enter a valid question.")
else:
    if name:
        print(f"{name} asks {question}")
    else:
        print(f"Question: {question}")
    print(f"Magic 8-Ball's answer: {answer}")