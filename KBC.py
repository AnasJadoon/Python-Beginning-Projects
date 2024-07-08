#Kon Bane Ga CrorePati
#Author: Muhammad Anas


# Questions = ["Who won the Champion's Trophy in 2017?", "Who is the Prime Minister of Pakistan?", "What is the name of the author of KBC?"]
# Answers1 = ['1.Pakistan', '2.India', '3.South Africa', '4.England']
# Answers2 = ['1.Imran Khan', '2.Gen. Asim Munir', '3.Nawaz Sharif', '4.Shahbaz Sharif']
# Answers3 = ['1.Muhammad Anas', '2.Anas Khan', '3.Muhammad Anas Khan Jadoon', '4.Jadoon']

# print("########WELCOME TO KON BANE GA CROREPATI!########")
# print("\nYour First Question is:\n\n", Questions[0])
# print("\nChoose a correct option!:\n")
# for i in Answers1:
#     print(i)

# x = int(input())
# if x == 1:
#     print("Congratulations! Your Answer is Correct!\n")
#     print("You've won 33 Lacs!")
# else:
#     print("Moye Moye! Better luck next time!")
#     print("We've an egg for you!")
#     exit()
# print("\nYour Second Question is:\n\n", Questions[1])
# print("\nChoose a correct option!:\n")
# for i in Answers2:
#     print(i)

# x = int(input())
# if x == 2:
#     print("Congratulations! Your Answer is Correct!\n")
#     print("You've won 67 Lacs!")
# else:
#     print("Moye Moye! Better luck next time!")
#     print("You still get 33 Lacs!")
#     exit()
# print("\nYour Third Question is:\n\n", Questions[2])
# print("\nChoose a correct option!:\n")
# for i in Answers3:
#     print(i)

# x = int(input())
# if x == 1:
#     print("Congratulations! Your Answer is Correct!\n")
#     print("You've won 1 Crore")
# else:
#     print("Moye Moye! Better luck next time!")
#     print("You were so close...! Don't Worry, take 67 Lac with you!")
#     exit()





#################################################         OR         ###########################################

import random


questions = [["What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3],
["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2],
["Who wrote 'Romeo and Juliet'?", "Charles Dickens", "Mark Twain", "William Shakespeare", "Jane Austen", 3],
["What is the chemical symbol for gold?", "Au", "Ag", "Pb", "Fe", 1],
["Who is known as the father of computers?", "Albert Einstein", "Isaac Newton", "Charles Babbage", "Thomas Edison", 3],
["What is the largest mammal in the world?", "Elephant", "Blue Whale", "Giraffe", "Hippopotamus", 2],
["What is the capital city of Japan?", "Seoul", "Beijing", "Tokyo", "Bangkok", 3],
["What is the hardest natural substance on Earth?", "Gold", "Iron", "Diamond", "Platinum", 3],
["Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", 3],
["Which country is known as the Land of the Rising Sun?", "China", "South Korea", "Thailand", "Japan", 4],
["What is the boiling point of water?", "90°C", "100°C", "110°C", "120°C", 2],
["Which element has the atomic number 1?", "Oxygen", "Carbon", "Hydrogen", "Nitrogen", 3],
["What is the largest continent?", "Africa", "Asia", "Europe", "Antarctica", 2],
["Who discovered penicillin?", "Marie Curie", "Alexander Fleming", "Louis Pasteur", "Joseph Lister", 2],
["What is the main ingredient in guacamole?", "Tomato", "Cucumber", "Avocado", "Pepper", 3]]

#shuffling options

for question in questions:
    question_text, *options, answer = question
    correct_option = options[answer - 1]
    random.shuffle(options)
    new_correct_answer = options.index(correct_option) + 1
    question[1:5] = options
    question[5] = new_correct_answer


questions.index(questions[5])
random.shuffle(questions)

points = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]

money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"Your Question {i+1} For Rs. {points[i]} Is:")
    print(f"\n{question[i-i]}")
    print(f"\n1. {question[1]}                       2. {question[2]}")
    print(f"\n3. {question[3]}                       4. {question[4]}")

    while True:
        try:
            print("\nEnter the correct answer within range 1-4")
            a = int(input())
            if (a<=4 and a>0): 
                if a == question[-1]:
                    money = points [i]
                    print("\n Correct Answer!")
                    if i == (len(questions) - 1):
                        print("\n\n                Congratulations! You Became Crore Pati !!!              ")
                else:
                    print(f"Moye Moye! The correct answer was {question[-1]}")
                    if (i == 4) or (i == 9) or (i == 14):
                        money = points [i]
                    elif 1 <= i < 5:
                        money = points [0]
                    elif 6 <= i < 10:
                        money = points [4]
                    elif 11 <= i < 15:
                        money = points [9]
                    print(f"Your take away money is Rs. {money}")
                    exit()
                break
            else:
                print("Answer is not within the mentioned range")
        except ValueError:
            print("Are you entering any other character?")

print(f"Your take away money is Rs. {money}")
 