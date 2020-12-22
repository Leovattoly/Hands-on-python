#This file contains a different type of definition(Scripts) for printing fibnocci

#script1-for printing fibnocci withonly one  parameter from the main function upto that number
def fib(n):
    a,b=0,1
    while a<n:
        print(a,end =' ')
        a,b=b,a+b
    print()

#script2-for printing fibnocci with only one parameter from the main function that is number of series
def fib2(n):
        k,a,b=0,0,1
        while k <= n-1:
            print (a,end=' ')
            a,b=b,a+b
            k=k+1
        print()

#script3-for returning series upto the number shared as parameter
def fib_return_series(n):
    result= []
    a,b=0,1
    while a<n:
        result.append(a)
        a,b=b,a+b
    return result

#script -3 for printing the fibnocci series upto n , varible passed via prg argument from the running #!/usr/bin/env python

if __name__=="__main__":
    import sys
    fib(int(sys.argv[1]))
