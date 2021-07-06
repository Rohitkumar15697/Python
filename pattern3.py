t=int(input('enter test cases:'))

x=0
y=0
while x<t:
        n=int(input('Enter size of patter only even number:'))

        if n%2==1:
                pass

        else:
                for i in range(0,2*n):
                        if i<n+1:
                                print('@',end='')
                        else:
                                print(' ',end='')
                                
                        if (i>=n/2 and i<2*n-n/2):
                                for j in range(n*(n-1)+1):
                                        
                                        print('*',end='')
                        else:
                                for j in range(n*(n-1)+1):
                                        print(' ',end='')

                        if i>=n-1:
                                print('@')
                        else:
                                print(' ')
                        
        x+=1
