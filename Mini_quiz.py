#Setting score count
score = 0


#Introducation for user taking the quiz
print("Welcome to the quiz!\n")


#First question with selected answers provided
answer1 = input("Q1. What is the capital of Canada?"
                    "\na. Toronto\nb. Ottawa\nc. Montreal\nd.Vancouver\nAnswer: ")

# Account for the different input the user enters
if answer1 == "b" or answer1 == "B" or answer1 == "Ottawa" or answer1 == "ottawa":
    score += 1
    print("You are correct!\n")  #Print the text for correct input, this concept repeats
else:
    print("Incorrect, the answer is Ottawa.\n") #Print the text for incorrect input, this concept repeats

print("Current Score: "+ str(score) + "\n")  #The score after this question and continue until end of page

answer2 = input("Q2. Which Canadian province has the highest population?"
                    "\na. Manitoba\nb. British Columbia\nc. Quebec\nd. Ontario\nAnswer: ")
if answer2 == "d" or answer1 == "D" or answer1 == "Ontario" or answer1 == "ontario":
    score += 1
    print("You are correct\n")
else:
    print("Incorrect, the answer is Ontario!\n")

print("Current Score: "+str(score) + "\n")

answer3 = input("Q3. What is the national animal of Canada?"
                    "\na. Moose\nb. Grizzly Bear\nc. Beaver\nd. Beluga Whale\nAnswer: ")
if answer3 == "c" or answer1 == "C" or answer1 == "Beaver" or answer1 == "beaver":
    score += 1
    print("You are correct\n")
else:
    print("Incorrect, the answer is Beaver!\n")

print(score)

answer4 = input("Q4. What is the capital city of Ontario?"
                    "\na. York\nb. Toronto\nc. Hamilton\nd. Peterborough\nAnswer: ")
if answer4 == "b" or answer1 == "B" or answer1 == "Toronto" or answer1 == "toronto":
    score += 1
    print("You are correct\n")
else:
    print("Incorrect, the answer is Toronto!\n")

print("Current Score: "+ str(score) + "\n")

answer5 = input("Q5. What province did not join Canada until 1949?"
                    "\na. Quebec\nb. British Columbia\nc. Newfoundland and Labrador\nd. Saskatchewan\nAnswer: ")
if answer5 == "c" or answer1 == "C" or answer1 == "Newfoundland and Labrador" or answer1 == "newfoundland and labrador":
    score += 1
    print("You are correct\n")
else:
    print("Incorrect, the answer is Newfoundland and Labrador!\n")

print("Current Score: "+ str(score) + "\n")

if score >=5:
    print("Excellent! " + str(score) + " /5") #Output when user score less than or equal to 5
elif score >=3:
    print("Good job, almost there.." + str(score) + "/5") #Output when user score less than or equal to 3
else:
    print("Need to study more! " + str(score) + "/5") #Output when user score
