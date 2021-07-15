def row_sum_odd_numbers(n):
    lenth = n
    counter=0
    while n>0:
        print((n, counter))
        counter+=n
        n-=1
    return (sum(range(1, counter*2, 2)[-lenth:]))
    #your code here

