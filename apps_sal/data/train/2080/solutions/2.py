m, mSale = int(input()), list(map(int,input().split()))
n, nPrice = int(input()), list(map(int,input().split()))
nPrice.sort()
sum, small = 0, min(mSale)

while True:
    if len(nPrice) <= small:
        for k in nPrice: sum+=k
        print(sum)
        return
    else:
        for i in range(small): sum+=nPrice.pop()
        if len(nPrice) <= 2:
            print(sum)
            return
        else:
            for i in range(2): nPrice.pop()
