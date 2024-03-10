import prompt

description = 'Answer "yes" if the number is even, otherwise answer "no".'

def even_game(num):
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    user_answer = prompt.string('Your answer: ')

    return [correct_answer, user_answer]