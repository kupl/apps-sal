# http://codeforces.com/contest/894/problem/0
# solved

array = input()
a = len(array)
o = 0

for i in range(a):
    if array[i] == "Q":
        for j in range(i + 1, a):
            if array[j] == "A":
                for k in range(j + 1, a):
                    if array[k] == "Q":
                        o += 1

print(o)
