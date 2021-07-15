n = int(input())
q = [0] * (n + 1)
t = list(map(int, input().split(" ")));
for i in t : q[i] = 1
s = ""
for i in range(1, n + 1) :
 if q[i] == 0 : s += str(i) + " "
print(s)
