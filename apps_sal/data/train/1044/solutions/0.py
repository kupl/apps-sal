number = int(input())
for i in range(number):
    a = list(input())
    for k in range(len(a)):
        a[k] = eval(a[k])
    print(sum(a))
