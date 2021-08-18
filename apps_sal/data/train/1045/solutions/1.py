t = int(input())
for _ in range(t):
    s = input()
    l1 = list()
    for i in s:
        l1.append(i)

    l2 = list()
    a = '0'
    b = '1'
    for i in l1:
        if i.isalpha():
            if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                l2.append(a)
            else:
                l2.append(b)

    l2 = ('').join(l2)
    x = ["0b", l2]
    x = "".join(x)
    x = eval(x)
    print(x)
