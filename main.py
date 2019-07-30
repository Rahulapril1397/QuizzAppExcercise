"""
    This is main code file.
"""
from quiz import Quiz, ObjectiveTest, SubjectiveTest

if __name__ == "__main__":
    QUIZ = Quiz()
    OBJECTIVETEST = ObjectiveTest()
    SUBJECTIVETEST = SubjectiveTest()
    QUIZ.genral_instruction()
    SUBJECTIVETEST.get_subjective_data()
    SUBJECTIVETEST.subjective_quiz()
    OBJECTIVETEST.get_objective_data()
    OBJECTIVETEST.objective_quiz()
    OBJECTIVETEST.performance()
 