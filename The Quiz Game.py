#Task 1

quiz_questions = ["In what state is Fort Knox located?",
"Who played Vincent Vega in Pulp Fiction?",
"What rock n roll band was famous for the hit Welcome to the Jungle?"]

quiz_answers = ["Kentucky", "John Travolta", "Guns N Roses"]


#Task 2

def quiz_game(questions, answers):
#Score starts at 0
    score = 0
    for i in range(len(questions)):
        print(f"Question {i+1}: {questions[i]}")
        user_answer = input("Your answer: ")
        if user_answer.lower() == answers[i].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Nope! The correct answer is {answers[i]}.")


#Task 3

    print(f"That's it! You got a score of: {score}/{len(questions)}. Good job!")
#Call the function
quiz_game(quiz_questions, quiz_answers)