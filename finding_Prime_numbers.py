n=int(input("Enter the limit of the numbers"))
for outer_loop in range(2,n+1):
    for inner_loop in range(2,outer_loop):
        if outer_loop % inner_loop == 0:
            print(outer_loop,'=',inner_loop,'*', outer_loop//inner_loop)
            break
    else:
        print(outer_loop,'is a prime number')
