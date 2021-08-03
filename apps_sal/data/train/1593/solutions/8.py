# cook your dish here
t = int(input())
while t != 0:
    n = int(input())
    ct = 0
    notes = [100, 50, 10, 5, 2, 1]
    i = 0
    while n:
        ct += n // notes[i]
        n = n % notes[i]
        i += 1
    print(ct)
    t = t - 1
