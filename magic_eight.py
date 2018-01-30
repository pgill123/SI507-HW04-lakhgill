# Purpose: Homework 4
# Collaborators: Preeti Gill, Wei Yun Chang,

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

# print("Possible responses:",magic)

def question ():
    input_answer = ""
    while (input_answer.upper() != "Q"):
        print("****************")
        print ("It's Magic Eight Ball time!")
        input_answer = input('Please enter your question for the Magic Eight Ball or "Q" to quit:\n')
        #Person A : Write code that checks if user input is a question (i.e., ends in a ‘?’) and,
        #if not, prints “I’m sorry, I can only answer questions.” (or something similar)
        #Edit the program so that it keeps asking for user input until the user inputs “quit”
        if "?" not in input_answer:
            while (input_answer.upper() != "Q" and  "?" not in input_answer):
                input_answer = input('I am sorry but I can only answer questions. Try again or enter "Q" to quit:\n')
        # Person B :　In the magic_eight.py file add code to pick an answer at random from the 20 possible 8 ball answers.
        # print("Your Question is: " + input_answer + ".")
        if input_answer == "Q":
            break
        random_answer = None
        num = randrange(0, 19)
        random_answer = magic[num]
        print("The answer is: " + random_answer + ".")




test = question()
