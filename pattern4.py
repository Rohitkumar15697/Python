n=int(input('enter the size of patter(enter only even number)'))

for i in range(0,n//2):
        for j in range(0,n//2-i):
                print(' ',end='')
                
        for j in range(0,2*i+1):
                print('*',end='')
        
        for j in range(2*n-2*i-1):
                print('.',end='')
        for j in range(0,2*i+1):
                print('*',end='')
        print()
for i in range(1):
        print(n*'*'+n*'@'+n*'*')

for i in range(0,n//2):
        for j in range(i+1):
                print(' ',end='')

        for j in range(0,n-2*i-2):
                print('*',end='')
                
        for j in range(n+2*i+2):
                print('.',end='')

        for j in range(0,n-2*i-2):
                print('*',end='')
        print()
