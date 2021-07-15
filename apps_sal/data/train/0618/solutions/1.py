# cook your dish here
inp = list(map(int,input().split()))
t = inp[0]
for te in range(t):
    inp = list(map(int,input().split()))
    n = inp[0]
    k = inp[1]
    inpp = list(map(int,input().split()))
    
    max = 0
    for i in range(k) :
        max = max + inpp[i%n]
        summ = max
    for j in range(0,n):
        summ = summ - inpp[j] + inpp[(j+k)%n]
        if summ >max :
            max = summ
    print(max)
