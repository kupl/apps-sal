# cook your dish heret
t = int(input())
w = []
for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    if len(set(s)) == len(s):
        w.append("prekrasnyy")
    else:
        w.append("ne krasivo")
for i in w:
    print(i)
