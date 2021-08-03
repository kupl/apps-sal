t = int(input())
while(t):
    s = input()
    if s == s[::-1]:
        print(1)
    else:
        print(2)
    t = t - 1
