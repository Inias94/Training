from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for questions in question_data:
    question = questions["text"]
    answer = questions["answer"]
    new_question = Question(question, answer)
    question_bank.append(new_question)

# print(question_bank[1].question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print(f"Quiz completed!\nFinal score: {quiz.score}/{len(quiz.questions_list)}")
