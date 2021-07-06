#Diamond

n=int(input('size of pattern'))
for i in range(0,n*2+1):
        if i<=n:
                for j in range(0,n-i):
                        print(' ',end='')
                for k in range(0,i+1):
                        print('* ',end='')
        else:
                for j in range(0,i-n):
                        print(' ',end='')
                for k in range(0,2*n+1-i):
                        print('* ',end='')
        print()
