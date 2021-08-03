# cook your dish here
try:
    from sys import stdin as si, stdout as so

    for _ in range(int(si.readline())):
        n, k = si.readline().split()
        a = set(n)
        so.write(str(len(a) ** 3) + '\n')
except:
    pass
