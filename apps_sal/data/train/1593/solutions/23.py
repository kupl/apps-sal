# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    c = 0
    sum = 0
    if(n >= 100):
        c = c + n // 100
        n = n % 100
    if(n >= 50):
        c = c + n // 50
        n = n % 50
    if(n >= 10):
        c = c + n // 10
        n = n % 10
    if(n >= 5):
        c = c + n // 5
        n = n % 5
    if(n >= 2):
        c = c + n // 2
        n = n % 2
    if(n >= 1):
        c = c + n // 1

    print(c)
