#CTI-110
#P4HW1 - Score List
#Emily McNerney
#April 24, 2023
#

# Creating an empty list
listOfScores = []

# Taking user input for numberOfScores
numberOfScores = int(input("How many numbers you want to enter? "))

# Initializing currentNumOfScores to 0
currentNumOfScores = 0

# Looping until we have all all required number of scores
while (True):

    # Looping for user input
    while (currentNumOfScores < numberOfScores):
        scores = float(input('Enter score #{}: '.format(currentNumOfScores + 1)))

        # Prompting for user input if entered score was invalid
        while (True):
            if (scores < 0 or scores > 100):
                print("\nINVALID Score entered!!!!\nScore should be between 0 and 100")
                scores = float(input('Enter score #{} again: '.format(currentNumOfScores + 1)))

            # If valid score was entered
            else:

                # Adding this to the list
                listOfScores.append(scores)

                # Breaking out of the loop as a valid score was
                # entered, no need for Prompting again
                break

        # Incrementing the count of currentNumOfScores by 1
        # when a valid score was entered
        currentNumOfScores += 1

        # If user entered all required number of valid scores
    if (currentNumOfScores == numberOfScores):
        # Breaking out of the loop as we do not require further input
        break

# Computing minimum score
minElement = min(listOfScores)

# Removing min score from the list
listOfScores.remove(min(listOfScores))

# Computing average score
average = sum(listOfScores) / len(listOfScores)

# Computing grade based on the average score
if (average >= 93 and average <= 100):
    grade = 'A'

elif (average >= 90 and average <= 92.9):
    grade = 'B+'

elif (average >= 87 and average <= 89.9):
    grade = 'B'

elif (average >= 83 and average <= 86.9):
    grade = 'B-'

elif (average >= 80 and average <= 82.9):
    grade = 'C+'

elif (average >= 77 and average <= 79.9):
    grade = 'C'

elif (average >= 73 and average <= 76.9):
    grade = 'C-'

elif (average >= 70 and average <= 72.9):
    grade = 'D+'

elif (average >= 67 and average <= 69.9):
    grade = 'D'

elif (average >= 60 and average <= 66.9):
    grade = 'D-'

elif (average < 59.9):
    grade = 'F'

# Displaying result on the console
print("--------------------Results----------------------")
print("Lowest Score  :", minElement)
print("Modified List :", listOfScores)
print("Scores Average:", average)
print("Grade         :", grade)
print("-------------------------------------------------")