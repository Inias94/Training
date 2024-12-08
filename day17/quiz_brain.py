class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.questions_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.question} (True/False ?):")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct")
            self.score += 1
            print(f"Current score: {self.score}/{len(self.questions_list)}")
        else:
            print(
                f"Wrong! The correct answer was: {correct_answer}\nCurrent score: {self.score}/{len(self.questions_list)}")
