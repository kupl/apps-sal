def thanks(n):
    if n < 10:
        print("Thanks for helping Chef!")
    else:
        print("-1")


t = int(input())
while t:
    t = t - 1
    n = int(input())
    thanks(n)
