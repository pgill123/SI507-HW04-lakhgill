# Purpose: Homework 4
# Collaborators: Preeti Gill,

from random import randrange

magic = [
'It is decidedly so'
,'Without a doubt'
,'Yes definitely'
,'You may rely on it'
,'As I see it, yes'
,'Most likely'
,'Outlook good'
,'Yes'
,'Signs point to yes'
,'Reply hazy try again'
,'Ask again later'
,'Better not tell you now'
,'Cannot predict now'
,'Concentrate and ask again'
,'Do not count on it'
,'My reply is no'
,'My sources say no'
,'Outlook not so good'
,'Very doubtful'
]

print("Possible responses:",magic)

def question ():
    input_answer = ""
    while (input_answer.upper() != "Q"):
        print("****************")
        print ("It's Magic Eight Ball time!")
        input_answer = input('Please enter your question for the Magic Eight Ball or "Q" to quit:\n')
        # Person B, I think you need to add your code here?

test = question()
