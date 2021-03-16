import os
import time
import random

def clear(): os.system('cls')

from os import system

system("title Magic 8 Ball")

print('Magic 8 Ball in Python Version 1.0')
print('''\
        ____
    ,dP9CGG88@b,
  ,IP  _   Y888@@b,
 dIi  (_)   G8888@b
dCII  (_)   G8888@@b
GCCIi     ,GG8888@@@
GGCCCCCCCGGG88888@@@
GGGGCCCGGGG88888@@@@...
Y8GGGGGG8888888@@@@P.....
 Y88888888888@@@@@P......
 `Y8888888@@@@@@@P'......
    `@@@@@@@@@P'.......
        """"........
    ''')
ballAnswers = ['It is certain', 'Without a doubt', 'You may rely on it', 'Yes, definitely', 'It is decidedly so', 'As I see it, yes', 'Most likely', 'Yes', 'Outlook good', 'Signs point to yes', 'Reply hazy, try again', 'Better not tell you now', 'Ask again later', 'Cannot predict now', 'Concentrate and ask again', 'Don\'t count on it', 'Outlook not so good', 'My sources say no', 'Very doubtful', 'My reply is no']
confirm = False
while confirm == False:
    print('Ask your yes or no question: ')
    question = input()
    clear()
    while confirm == False:
        print('You asked: "' + question + '", is that correct?')
        print('Type "yes" to confirm, or type anything else to go back')
        conf = input()
        if conf.lower() == 'yes':
            clear()
            confirm = True
            print('Your question is confirmed. Shaking the 8 ball...')
            time.sleep(2)
            break
        else:
            print('Ok, you can try again! Ask your yes or no question: ')
            question = input()
            continue
    look = False
    shakes = 1
    while look == False:
        roll = random.randint(0,19)
        clear()
        print('You shook the 8 ball ' + str(shakes) + ' time' + ('s' if shakes != 1 else '') + ', shake again?')
        print('Type "shake" to shake again or type "look" to look at your answer.')
        shakeChoice = input()
        if shakeChoice.lower() == 'shake':
            clear()
            print('Shake, shake, shake!')
            shakes = shakes + 1
            time.sleep(2)
            continue
        elif shakeChoice.lower() == 'look':
            clear()
            print('The blue answer die floats toward the viewing window...')
            time.sleep(3)
            print(question + '\n' + ballAnswers[roll])
            look = True
            break
        else:
            print('Sorry, that wasn\'t a valid option. Please try again...')
            time.sleep(2)
            clear()
            continue
    time.sleep(2)
    print('Would you like to ask another question?')
    yesOrNo = input()
    if yesOrNo.lower() != 'yes' and yesOrNo.lower() != 'no':
        problemChild = True
        while problemChild == True:
            print('Sorry, we just need a simple "yes" or "no", would you like to ask another question?')
            yesOrNo = input()
            if yesOrNo.lower() == 'yes':
                clear()
                confirm = False
                problemChild = False
            elif yesOrNo.lower() == 'no':
                print('Thanks for playing. Goodbye!')
                problemChild = False               
            continue
    elif yesOrNo.lower() == 'no':
        print('Thanks for playing. Goodbye!')
        break
    elif yesOrNo.lower() == 'yes':
        clear()
        confirm = False
        continue