def max_multiple(divisor, bound):
    list_ans = []
    for i in range(0,bound+1):
        if i % divisor == 0:
            list_ans.append(i)
    return max(list_ans)

