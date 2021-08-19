# cook your dish here
def colour(s):
    c = 0
    for i in range(len(s) - 1):
        if(i == len(s) - 1):
            break
        if (s[i] == s[i + 1]):

            c += 1
    print(c)


t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    colour(s)
