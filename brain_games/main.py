from cli import welcome_user
from get_random_num import get_random_num

def main(description, round):
    print("Welcome to the Brain Games!")

    name = welcome_user()
    
    print(description)

    count_round = 1

    while count_round <= 3:
        random_num = get_random_num()
        print(f"Question: {random_num}")

        [correct_answer, user_answer] = round(random_num)

        if correct_answer != user_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
        print("Correct!")

        count_round += 1
    
    print(f"Congratulations, {name}!")