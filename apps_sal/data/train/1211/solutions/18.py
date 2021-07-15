# cook your dish here
try:
    t = int(input())
    for _ in range(t):
        N = input()
        for i in range(len(N)):
            N = N.replace('abc', '')
        print(N)         
except:
    pass

