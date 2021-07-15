
cases = int(input())

for i in range(cases):
    a1, d, uG, oG = list(map(int, input().split()))
    a1 = a1 %9 if a1 %9 != 0 else 9
    d = d %9 if d %9 != 0 else 9
    sum_of = 0
    rest_of = 0
    q = (a1 +d *(uG -1)) %9 if (a1 +d *(uG -1)) %9 !=0 else 9
    q1 = q
    k = (oG - uG) %9
    f = int((oG - uG) /9)
    
    for j in range(uG, uG +9):
        sum_of += q
        q += d
        q = q %9 if q %9 != 0 else 9
    
    for k in range(uG, uG +k +1):
        rest_of += q1
        q1 += d
        q1 = q1 %9 if q1 %9 != 0 else 9

    print(sum_of *f +rest_of)

