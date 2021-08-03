t = int(input())
for i in range(t):
    n = int(input())
    term = (-1 + ((8 * n + 9)**0.5)) / 2
    # print('term is '+str(term))
    if term == int(term):
        ans = int(term - 1)
        # print('yo')
        # print(str(term)+' '+str(int(term)))
    else:
        term = int(term)
        summ = ((term * (term + 1)) // 2) - 1
        # print('summ is '+str(summ))
        ans = n - summ - 1
    print(ans)
