t = int(input())
for i in range(t):
    cnt = 0
    n = int(input())
    while(n >= 100):
        n -= 100
        cnt += 1
    while(n >= 50):
        n -= 50
        cnt += 1
    while(n >= 10):
        n -= 10
        cnt += 1
    while(n >= 5):
        n -= 5
        cnt += 1
    while(n >= 2):
        n -= 2
        cnt += 1
    while(n >= 1):
        n -= 1
        cnt += 1
    print(cnt)
