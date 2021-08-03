import sys
input = sys.stdin.readline


def stringminus(s):
    i = -1
    n = len(s)
    s2 = ["0"] * n
    for j in range(n):
        s2[j] = s[j]
    while s[i] == "0":
        s2[i] = "1"
        i -= 1
    s2[i] = "0"
    sol = s2[0]
    for i in range(1, n):
        sol += s2[i]
    return sol


def stringplus(s):
    i = -1
    n = len(s)
    s2 = ["0"] * n
    for j in range(n):
        s2[j] = s[j]
    while s[i] == "1":
        s2[i] = "0"
        i -= 1
    s2[i] = "1"
    sol = s2[0]
    for i in range(1, n):
        sol += s2[i]
    return sol


for f in range(int(input())):
    rem = set()
    med = "0"
    isc = 0
    n, m = map(int, input().split())
    for i in range(m - 1):
        med += "1"
    for i in range(n):
        s = input()
        s = s[0:m]
        if s > med:
            isc += 1
        if s < med:
            isc -= 1
        if s == med:
            if isc == 0:
                isc = -1
            else:
                isc = 2
        rem.add(s)
        if isc == -1:
            med = stringplus(med)
            while med in rem:
                med = stringplus(med)
            isc = 1
        if isc == 2:
            med = stringminus(med)
            while med in rem:
                med = stringminus(med)
            isc = 0
    print(med)
