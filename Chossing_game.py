import random
import os
import time

wanna_cont = True

while wanna_cont == True:

    os.system('cls' if os.name == 'nt' else 'clear')

    possibles_words = ["python", "programacao", "desenvolvimento", "computador", "algoritmo"]
    word = possibles_words[random.randint(0,len(possibles_words))]
    hidden = ['_'] * len(word)


    print('━' * 20)
    for i in 'WELCOME TO GUESSING GAME!!!':
        time.sleep(0.1)
        print(i, end= "")
    print(f'\n{'━' * 20}\nYour word is: {''.join(hidden)}')



    while True:
        letter = str(input('Enter the letter: ')).lower()
        index = -1

        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    hidden[i] = letter 
            print(''.join(hidden))
            
            if '_' not in hidden:
                os.system('cls')    
                for i in range (0,9):
                    time.sleep(0.3)
                    print('.', end="")
                print("YOU WIN!")

                
                if input('You wanna continue?[Y/N]: ').upper() == 'N':
                    print('BYE',end= "")
                    for i in range(0,10):
                        time.sleep(0.1)
                        print('E',end= "")
                    wanna_cont = False

                break

            else:
                continue

        else:
            print('The letter is not in the word, try again. ')
            print(''.join(hidden))
            continue

