# cook your dish here
try:
    t = int(input())
    for i in range(t):
        s = input()
        i = int(s, 16)
        print(i)
except EOFError as e:
    print(e)
