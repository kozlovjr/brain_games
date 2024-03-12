import prompt 
import random
from ..get_random_num import get_random_num

description = 'What is the result of the expression?'

def calc_game():
    first_num = get_random_num()
    second_num = get_random_num()

    arithmetic_operations = ['+', '-', '*']
    operation = random.choice(arithmetic_operations)

    question = f"Question: {first_num} {operation} {second_num}"
    print(question)

    if operation == "+":
        correct_answer = first_num + second_num
    if operation == "-":
        correct_answer = first_num - second_num
    else:
        correct_answer = first_num * second_num
    
    user_answer = prompt.integer("Your answer: ")

    return [correct_answer, user_answer]