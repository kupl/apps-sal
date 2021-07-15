

def square_sum(numbers):
    sum=0
    x=len(numbers)
    for i in range(x):
        a=pow(numbers[i], 2)
        sum=a+sum
    return sum
