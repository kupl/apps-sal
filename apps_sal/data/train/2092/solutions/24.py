n = int(input())
airp = input()
dep = []
arr = []
for i in range(n):
    t = input().split("->")
    dep.append(t[0])
    arr.append(t[1])

if n % 2 == 1:
    print("contest")
else:
    if dep.count(airp) == arr.count(airp):
        print("home")
    else:
        print("contest")
