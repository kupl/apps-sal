# cook your dish here
x = int(input())
li = []
for i in range(x):
    y = int(input())
    li.append(int(y))
li.sort()
for i in li:
    print(i)
