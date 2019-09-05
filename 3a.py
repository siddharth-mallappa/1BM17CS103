def check(n):
    for i in range(1,int(n/2)+1):
        if(n%i==0):
            print (i)

a=int(input("enter a number"))
check(a)
