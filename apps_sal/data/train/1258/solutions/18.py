# cook your dish here
for u in range(int(input())):
    n = input()
    s = sum(map(int, n))
    if(len(n) > 1 and s < 5):
        print(9 - s)
    else:
        print(min(s % 9, 9 - s % 9))
