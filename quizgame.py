question_data = [
    {"question": "The Earth revolves around the Sun.", "correct_answer": "True"},
    {"question": "Python is named after a snake.", "correct_answer": "False"},
    {"question": "Water freezes at 0 degrees Celsius.", "correct_answer": "True"},
    {"question": "The capital of France is Berlin.", "correct_answer": "False"},
    {"question": "Light travels faster than sound.", "correct_answer": "True"}
]
class Question:
    def __init__(self,q_que,answer):
        self.q_que=q_que
        self.answer=answer
class QuizBrain:
    def __init__(self,q_list):
        self.q_list=q_list
        self.que_no=0
        self.score=0
    def check_ans(self,userans,correctans):
        if userans.lower() == correctans.lower():
            self.score+=1
            print("You are right.")
        else: 
            print("You are wrong.")
        print(f"correct answer was {correctans} ")
        print(f"your current score is {self.score}")
    def ifnextque(self):
        currentques=self.q_list[self.que_no]
        self.que_no+=1
        userans=input(f"Q.{self.que_no}: {currentques.q_que} (True/False): ")
        self.check_ans(userans,currentques.answer)
que_list=[]
for x in question_data:
    q_que = x["question"]
    answer = x["correct_answer"]
    newquehehe = Question(q_que,answer)
    que_list.append(newquehehe)
quiz=QuizBrain(que_list)
while quiz.que_no < len(que_list):
    quiz.ifnextque()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.que_no}")


    
    
