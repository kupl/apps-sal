# oimv
d = int(input())
for tt in range(d):
    n = int(input())
    s = list(map(int, input().split()))
    x = int(input())
    sum = []
    count = 0
    low = -1
    high = n
    if(n == 1):
        print("1 0")
        continue
    counta = 0
    countb = 0
    timea = 0
    timeb = 0
    while(1):
        if(low >= high - 1):
            break
        if timea < timeb:
            low += 1
            timea += s[low] / x
            counta += 1
        elif timea > timeb:
            high -= 1
            timeb += s[high]
            countb += 1
        else:
            if counta >= countb:
                low += 1
                timea += s[low] / x
                counta += 1
            else:
                high -= 1
                timeb += s[high]
                countb += 1
    print(counta, countb)
