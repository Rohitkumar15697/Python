n=int(input('Enter the size of pattern'))

if n%2==0:
        pass

else:
        #Upper half
        for i in range(0,n-1):
                print('*',end='')
                
                for j in range(0,2*n-2):

                        if (j>=0 and j<n-2):
                                print(' ',end='')
                        elif j==n-2:
                                print('*',end='')

                        if i==0 and j>=n-1:
                                print('*',end='')


                                
                
                print()

        #middle line
        for i in range(1):
                print((2*n-1)*'*')


        #lower half
        for i in range(0,n-1):


                for j in range(0,2*n):
                        
                        if (j>=0 and j<n-1):
                                if i==n-2:
                                        print('*',end='')
                                else:
                                        print(' ',end='')
                        elif j==n:
                                print('*',end='')

                        elif (j>n and j<2*n-1):
                                print(' ',end='')

                        elif j==2*n-1:
                                print('*',end='')
                print()










        
