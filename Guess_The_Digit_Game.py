import random
import time

class SignIn:
    def __init__(self,name,points):
        '''
            This is a guess the digit game. In this game you have to guess the digit between 0 to 6 and if 
            out of 3 random numbers your digit matches count times, your points will be increased by count else
            your point decreased by one

        '''
        self.name=name
        self.points=points
        print(f'You are logged In {self.name}')
        


#This is player1
class Python(SignIn):
    def Attack(self):
        self.count=0
        python_point=int(input(f'{self.name} Guess the digit between 0 to 6 ??:  '))
        count=random_list.count(python_point)
        if  count>0:
            self.points+=count
            
        else:
            self.points-=1
            

        

#This is player2
class Cobra(SignIn):
    def Attack(self):
        self.count=0
        cobra_point=int(input(f'{self.name} Guess the digit between 0 to 6 ??:  '))
        count=random_list.count(cobra_point)
        if  count>0:
            self.points+=count
        
        else:
            self.points-=1
          



#Taking input player names

first_player=input(' Player1 ').capitalize()

second_player=input(' player2 ').capitalize()


#Creating Objects
player1=Python(first_player,10)
player2=Cobra(second_player,10)

#print(help(SignIn))

print(f'{player1.name} has {player1.points} points')
print(f'{player2.name} has {player2.points} points')


#Rounds Loop

n=int(input('how much rounds you want to play: '))
for i in range(1,n+1):
    print(f'\nRound {i}')
    random_list=[]
    for j in range(3):
        
        #Generate random numbers list
        random_list.append(random.randint(0,6))
    
    player1.Attack()
    player2.Attack()
    
    print(f'{player1.name} - {player1.points}')
    print(f'{player2.name} - {player2.points}')
    print(f'random number {random_list}')
    print()


print('Player       points')
print(f'{player1.name}          {player1.points}')
print(f'{player2.name}          {player2.points}')

print()
#Condition for winner player
if player1.points > player2.points:
    print(f'{player1.name} is winner !!!!')


elif player1.points==player2.points:
    print(f'There is a tie between {player1.name} and {player2.name}')


else:
    print(f'{player2.name} is winner !!!!')

time.sleep(5)


    

