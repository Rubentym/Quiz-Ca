class QuizCategory:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

quiz_categories = {
    "General Knowledge": general_knowledge_questions,
    "Mathematics": math_questions,
    "Science": science_questions
}
