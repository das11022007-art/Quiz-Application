questions = {
    "What is the capital city of Pakistan" : "Islamabad",
    "2 + 2 = ?" : "4",
    "What is the color of the sky?" : "Blue",
    "What is the largest mammal?" : "Blue Whale",
    "Python is a programming language?": "Yes"
}   

score = 0
for question in questions:
    print(question)

    answer = input("Enter your answer: ")
    if answer.lower() == questions[question].lower():
        print("Correct Answer: ")
        score = score + 1
    else:
        print("Incorrect Answer: ")

print("\n -----QUIZ END----")
print("Final score : ", score)
    