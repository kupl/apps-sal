# cook your dish here
def primefun(n):
    seive = [1 for i in range(n + 1)]
    i = 2
    while(i * i <= n + 1):
        if seive[i] == 1:
            for j in range(i * i, n + 1, i):
                seive[j] = 0
        i = i + 1
    seive[0] = 0
    seive[1] = 0
    return seive


def divide(n, seive):
    #print('divide n is',n)
    for i in range(2, n, 1):
        if(n % i == 0):
            #print('n%i is',i)
            if(seive[i] == 1 and seive[n // i] == 1):
                if i != n // i:
                    return True


count = int(input())
for g in range(count):
    n = int(input())
    flag = 0
    seive = primefun(n)
    for i in range(6, n):
        if(i + (n - i) == n):
            # print(i,n-i)
            k = n - i
            if divide(i, seive) == True and divide(k, seive) == True:
                flag = 1
                print('YES')
                break
    if flag == 0:
        print('NO')
