#Setting score count
score = 0

#Introducation for user taking the quiz
print("Welcome to the quiz! Canadian Edition!\n")

#First question with selected answers provided
answer1 = input("Q1. What is the capital of Canada?"
                    "\na. Toronto\nb. Ottawa\nc. Montreal\nd.Vancouver\nAnswer: ")

# Account for the different input the user enters when request
if answer1 == "b" or answer1 == "B" or answer1 == "Ottawa" or answer1 == "ottawa":
    score += 1
    print("You are correct!\n")  #Print the output for correct input, this concept repeats for next question
else:
    print("Incorrect, the answer is Ottawa.\n") #Print the output for incorrect input, this concept repeats for next question

print("Current Score: "+ str(score) + "\n")  #The score is counted after this question and continue until end of page for final score

answer2 = input("Q2. Which Canadian province has the highest population?"
                    "\na. Manitoba\nb. British Columbia\nc. Quebec\nd. Ontario\nAnswer: ")
if answer2 == "d" or answer2 == "D" or answer2 == "Ontario" or answer2 == "ontario":
    score += 1
    print("You are correct\n")
else:
    print("Incorrect, the answer is Ontario!\n")

print("Current Score: "+str(score) + "\n")

answer3 = input("Q3. What is the national animal of Canada?"
                    "\na. Moose\nb. Grizzly Bear\nc. Beaver\nd. Beluga Whale\nAnswer: ")
if answer3 == "c" or answer3 == "C" or answer3 == "Beaver" or answer3 == "beaver":
    score += 1
    print("You are correct\n")
else:
    print("Incorrect, the answer is Beaver!\n")

print(score)

answer4 = input("Q4. What is the capital city of Ontario?"
                    "\na. York\nb. Toronto\nc. Hamilton\nd. Peterborough\nAnswer: ")
if answer4 == "b" or answer4 == "B" or answer4 == "Toronto" or answer4 == "toronto":
    score += 1
    print("You are correct\n")
else:
    print("Incorrect, the answer is Toronto!\n")

print("Current Score: "+ str(score) + "\n")

answer5 = input("Q5. What province did not join Canada until 1949?"
                    "\na. Quebec\nb. British Columbia\nc. Newfoundland and Labrador\nd. Saskatchewan\nAnswer: ")
if answer5 == "c" or answer5 == "C" or answer5 == "Newfoundland and Labrador" or answer5 == "newfoundland and labrador":
    score += 1
    print("You are correct\n")
else:
    print("Incorrect, the answer is Newfoundland and Labrador!\n")

print("Current Score: "+ str(score) + "\n")

if score >=5:
    print("Excellent! " + str(score) + " /5") #Output when user score 4 and above
elif score >=3:
    print("Good job, almost there.." + str(score) + "/5") #Output when user score  or equal to 3
else:
    print("Need to study more! " + str(score) + "/5") #Output when user score 3 and below
