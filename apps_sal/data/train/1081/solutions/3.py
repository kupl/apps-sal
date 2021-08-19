# cook your dish here
for x in range(int(input())):
    n = list(input())
    l = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    list1 = [98, 57, 31, 45, 46]
    c = 0
    for i in range(0, len(n)):
        for j in range(0, len(l)):
            if n[i] == l[j]:
                s1 = j + list1[c]
                s2 = s1 % 26
                print(l[s2], end="")
        c += 1
    print("\n")
