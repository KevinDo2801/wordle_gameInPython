import random

print('''# (C) means the letter is in the word and in the correct position
# (WP) mean the letrer is in the word but not in the correct position
# (NT) means the letter is not there in the word it self''')

words = ["this", "five", "help", "lake", "pink", "cats"]

hidden_word =random.choice(words)

def check_word(guess):
    if hidden_word == guess:
        print("Yeah")
        return True
    else:
        result = ''
        for i,j in zip(guess, hidden_word):
            if i == j:
                result += "(C)"
            elif i in hidden_word:
                result += "(WP)"
            else:
                result += "(NT)"
        print(result)
        return False

def main():
    attempt = 5
    while attempt > 0:
        guess = input("Guess a four letterd word: ")
        if check_word(guess):
            break
        else:
            attempt -= 1
            print(f'You have {attempt} attemps left.')

main()
