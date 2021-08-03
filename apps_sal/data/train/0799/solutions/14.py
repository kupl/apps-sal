# cook your dish here
c = 0
for _ in range(int(input())):
    s = input()
    if s.count('1') >= 2:
        c = c + 1
print(c)
