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
while !confirm:
    print('Ask your yes or no question: ')
    question = input()
    clear()
    while !confirm:
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
            continue
    break

