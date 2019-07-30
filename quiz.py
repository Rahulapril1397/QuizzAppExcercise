"""
    Quiz, Subective and Objestive test class.
"""
import pandas as pd

class Quiz:
    """
       General Informationa about quiz, and input name.
    """

    def __init__(self):
        """
            THis is doc string
        """
        self.answer = []
        self.name = None
        self.df_subjective = None
        self.df_objective = None

    def genral_instruction(self):
        """
            Print ou the genral instruction about the test.
        """
        self.name = input("Enter your name:")
        print("General Instrucion for the test.")
        print("A. In total there are 20 questions.")
        print("B. There are two types of questions subjective and objective.")
        print("C. There are 10 subjective questions carrying 1 marks each.")
        print("D. There are 10 objective questions.")
        print("First attempt subjective questions")
        print("E. For objective questions reponses should be anyone of A, B, C or D ")
        print("F. Attempt all questions.")

    def objective_quiz_data(self):
        """
            Stores the csv file of objective question in dataframe.
        """
        self.df_objective = pd.read_csv('Objective.csv')
        return self.df_objective

    def subjective_quiz_data(self):
        """
            Stores the csv file of subjective question in dataframe.
        """
        self.df_subjective = pd.read_csv('subjective_questions.csv', sep='\t')
        return self.df_subjective

    def user_answer(self):
        """
            Stores the answer input by the user.
        """
        #for inputs in range(0, 1):
        self.answer.append(input("Your Answer: "))
        return self.answer

class ObjectiveTest(Quiz):
    """
        Ask objective question one by one and stores the input given by the user.
    """

    def __init__(self):
        Quiz.__init__(self)
        self.answer_objective = None
        self.score_obtained = None
        self.correct_answer_data = None
        self.df_objective_data = None
        self.marks = 0

    def get_objective_data(self):
        """
            This is doc string.
        """
        self.df_objective_data = Quiz.objective_quiz_data(self)

    def objective_quiz(self):
        """
            Ask the question from the stored dataframe
        """
        for row in range(0, 10):
            objective_question = self.df_objective_data.loc[row, "Questions"]
            objective_option_a = self.df_objective_data.loc[row, "A"]
            objective_option_b = self.df_objective_data.loc[row, "B"]
            objective_option_c = self.df_objective_data.loc[row, "C"]
            objective_option_d = self.df_objective_data.loc[row, "D"]

            print("Question: ", objective_question)
            print("Opt A:", objective_option_a)
            print("Opt B:", objective_option_b)
            print("Opt C:", objective_option_c)
            print("Opt D:", objective_option_d)

            self.answer_objective = Quiz.user_answer(self)

    def performance(self):
        """
            Compare the response of the user and the correct answer and oututs the score.
        """
        self.correct_answer_data = self.df_objective_data.loc[:, "Answer"]
        for i in range(0, 10):
            if self.answer_objective[i] == self.correct_answer_data[i]:
                self.marks += 1
        print("Your responses", self.answer_objective)
        print("Answer key", self.correct_answer_data)
        print("score", self.marks)


class SubjectiveTest(Quiz):
    """
        Ask objective question one by one and stores the input given by the user.
    """

    def __init__(self):
        """
            Initializes class attributes.
        """
        Quiz.__init__(self)
        self.answer_subjective = None
        self.df_subjective_data = None

    def get_subjective_data(self):
        """
            Reads the subjective csv file using method of parent class Quiz.
        """
        self.df_subjective_data = Quiz.subjective_quiz_data(self)

    def subjective_quiz(self):
        """
            Ask subjective questions
        """
        for row in range(0, 10):
            subjective_question = self.df_subjective_data.loc[row, "Questions"]

            print("Question: ", subjective_question)

            self.answer_subjective = Quiz.user_answer(self)

            print("Correct Answer:" + self.df_subjective_data.loc[row, "Answers"])
