n,A,cf,cm,mN = list(map(int,input().split()))

a = list(map(int,input().split()))
aCOPY = []
for elem in a:
    aCOPY.append(elem)
a.sort()

aPartialSum = [0]

for elem in a:
    aPartialSum.append(aPartialSum[-1] + elem)

maxScore = 0
ansMAXIBound = 0
ansMAXI = 0
ansMIN = 0
for MAXI in range(n + 1):
    currentScore = cf * MAXI
    if MAXI >= 1:
        mN -= (A - a[-MAXI])
    if mN < 0:
        break
    if MAXI == n:
        maxScore = currentScore + A * cm
        ansMAXIBound = 0
        ansMAXI = 10 ** 10
        ansMIN = 0
    # Find the maximum of minimum
    l = a[0]
    r = A - 1

    while l < r:
        m = (l + r + 1) // 2
        lA = 0
        rA = n - MAXI - 1
        while lA < rA:
            mA = (lA + rA) // 2
            if a[mA] > m:
                rA = mA - 1
            if a[mA] < m:
                lA = mA + 1
            if a[mA] == m:
                lA = mA
                rA = mA
                break
        lA = min(lA,n - MAXI - 1)
        if a[lA] > m:
            lA -= 1
        expenditure = (lA + 1) * m - aPartialSum[lA + 1]
        if expenditure > mN:
            r = m - 1
        else:
            l = m
    currentScore += l * cm
    if currentScore > maxScore:
        maxScore = currentScore
        ansMAXIBound = a[-MAXI]
        ansMAXI = MAXI
        ansMIN = l

print(maxScore)
inclCount = 0
for i in range(n):
    if aCOPY[i] > ansMAXIBound and inclCount < ansMAXI:
        aCOPY[i] = A
        inclCount += 1
for i in range(n):
    if aCOPY[i] == ansMAXIBound and inclCount < ansMAXI:
        aCOPY[i] = A
        inclCount += 1
    if aCOPY[i] < ansMIN:
        aCOPY[i] = ansMIN
print(" ".join(map(str,aCOPY)))


