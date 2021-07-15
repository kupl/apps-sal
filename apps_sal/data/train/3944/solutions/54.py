def sum_triangular_numbers(n):
    if n <=0:
        return 0
    li= [1]
    for i in range(2,n+1):
        li.append(li[-1]+i)
    return sum(li)
