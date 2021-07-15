def square_sum(numbers):
    #your code here
    g=0
    for i in range(len(numbers)):
        g+=pow(int(numbers[i]),2)
    return g 
