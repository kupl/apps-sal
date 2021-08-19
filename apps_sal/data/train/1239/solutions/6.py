# cook your dish here
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
for k in range(len(a)):
    for w in range(a[k] + 1):
        nct = a[k] - w
        nqt = w + 1
        for i in range(nct):
            print(" ", end="")
        for j in range(nqt):
            print(a[k] - j, end="")
        print()

    for w in range(a[k] + 1):
        nqt = a[k] - w
        nct = w + 1
        for i in range(nct):
            print(" ", end="")
        for j in range(nqt):
            print(a[k] - j, end="")
        print()
