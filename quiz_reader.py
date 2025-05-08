# Program parts

# Import necessary modules
import random

# Define ANSI color codes for output
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Define a function to load and parse quiz questions from file
def load_questions(filename):
    with open(filename, "r") as file:
        lines = [line.strip() for line in file if line.strip() != ""]

    questions = []
    i = 0
    while i < len(lines):
        if lines[i].startswith("Question:"):
            question_text = lines[i][len("Question: "):]
            choice_a = lines[i+1][len("A. "):]
            choice_b = lines[i+2][len("B. "):]
            choice_c = lines[i+3][len("C. "):]
            choice_d = lines[i+4][len("D. "):]
            correct = lines[i+5][len("Correct Answer: "):].upper()

            questions.append({
                "question": question_text,
                "A": choice_a,
                "B": choice_b,
                "C": choice_c,
                "D": choice_d,
                "correct": correct})
            i += 6
        else:
            i += 1
    return questions

# Main program logic
def run_quiz():
    questions = load_questions("quiz_questions.txt")
    if not questions:
        print(f"{RED}No questions found. Please add questions using the Quiz Creator.")
        return

# Run the quiz