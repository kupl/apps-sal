(name1, name2) = input().split()
n = int(input())
for i in range(n):
    print(name1, name2)
    (killed, new) = input().split()
    if killed == name1:
        name1 = new
    else:
        name2 = new
print(name1, name2)
