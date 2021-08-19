# cook your dish here
for k in range(int(input())):
    leng, cont, val = map(int, input().split())
    temp = cont * [0]
    temp[0] = val
    ans0 = (leng // cont) * temp + temp[:leng % cont]
    ans = ' '.join([str(x) for x in ans0])
    print(ans)
