t = eval(input())
for i in range(t):
    string = input()
    l = len(string)
    aset = set()
    for i in range(l - 1):
        aset.add(string[i:i + 2])
    print(len(aset))
