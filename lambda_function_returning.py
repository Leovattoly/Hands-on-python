def sum_of_args(a):
    return lambda b:a+b #a=a+b
obj=sum_of_args(1) # creating function object
print(obj(2)) # calling fucntion using the fucntion object
print(obj(22))
