import random
# New code 1
score = 0
def addition (score):

    number_1 = random.randrange(1,100)
    number_2 = random.randrange(1,100)
    correct_answer = number_1 + number_2
    question = "Addition Question "+str(Q_1)+ ". What is "+str(number_1)+" + "+str(number_2) + " = "
    user_answer = int(input(question))
    if user_answer == correct_answer:
        # New Code
       score = score + 1

       print("Correct :)")
    else:
        print("Wrong >:(")
    return score



def subtraction (score):
    number_1 = random.randrange(1,100)
    number_2 = random.randrange(1,100)
    correct_answer = number_1 - number_2
    question = "Subtraction Question "+str(Q_1)+ ". What is "+str(number_1)+" - "+str(number_2) + " = "
    user_answer = int(input(question))
    if user_answer == correct_answer:
        # New Code
        score = score + 1

        print("Correct :)")
    else:
        print("Wrong >:(")
    return(score)
for Q_1 in range (1,12):
    score = addition(score)
    score = subtraction(score)

for i in range (1,score):
    print (":)")


print("You got "+str(score)+" out of 24")

#Fixed by Tobi