def print_even_no(a):
    for i in range(2,a+1):
        if i % 2 ==0:
            print(i,' is an even number')
            continue
a=int(input("Enter the limit"))
print_even_no(a)
