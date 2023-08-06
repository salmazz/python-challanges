import json
import random

with open('questions.json', 'r') as file:
    content = file.read()
data = json.loads(content)

random.shuffle(data)  # Randomize the order of questions

score = 0

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    while True:
        try:
            user_choice = int(input("Enter Your Choose: "))
            if 1 <= user_choice <= len(question["alternatives"]):
                break
            else:
                print("Invalid choice. Please enter a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    question["user_choice"] = user_choice

    if user_choice == question['correct_answer']:
        score += 1
        print("Correct Answer!\n")
    else:
        print("Wrong Answer!\n")

print("=== Quiz Finished ===")
print("Your Final Score:", score, "/", len(data))

# Provide overall feedback based on the user's score
if score == len(data):
    print("Congratulations! You answered all questions correctly!")
elif score == 0:
    print("Oops! You didn't answer any questions correctly. Keep practicing!")
else:
    print("Well done! You answered", score, "out of", len(data), "questions correctly.")
