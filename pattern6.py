n=int(input('Enter the size of pattern:'))
for i in range(0,(n//2)+1):
        for j in range(0,i):
                print(' ',end='')

        for j in range(0,n-2*i):
                print('*',end='')

        print()

for i in range(0,(n//2)):
        for j in range(n//2-i-1):
                print(' ',end='')
        for j in range(0,2*i+3):
                print('*',end='')
        print()
                      
