import prompt
from ..get_random_num import get_random_num

description = 'Find the greatest common divisor of given numbers.'

def found_gcd(num1, num2):
    if(num1 > num2):
        [first_num, second_num] = [num1, num2]
    else: 
        [first_num, second_num] = [num1, num2]
    
    
    if first_num % second_num == 0: # basic case
        print(second_num)
    
    else: # resursive case
        found_gcd(first_num, first_num % second_num)

def gcd_game():
    first_num = get_random_num()
    second_num = get_random_num()

    print(f"Question: {first_num} {second_num}")

    correct_answer = found_gcd(first_num, second_num)
    user_answer = prompt.integer("Your answer: ")

    return [correct_answer, user_answer]
