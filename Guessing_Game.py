import random
import time
import sys

def random_guessing():
    number=random.randint(1,10)
    print('random number ',number)
    while True:
        try:
            my_input=int(input('Input '))
            if my_input>=1 and my_input<=10:
                if my_input==number:
                    print('Hurrrayyy..... You are a Genius ...')
                    break
                else:
                    print('Try Again')
                    continue
            else:
                print('Hey bro, I said Enter 1~10')
                continue
        except ValueError:
            print('Please enter a number')
            continue


random_guessing()


while True:
    try:
        x=input('You want to play again [Y/N]').lower()
        if x=='y':
            random_guessing()
            continue
        elif x=='n':
            print('Exit')
            sys.exit()
    except ValueError:
        print('Try to enter Y/N')
        continue
    
time.sleep(5)
        


