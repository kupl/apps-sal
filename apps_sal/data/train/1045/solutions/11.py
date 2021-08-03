# cook your dish here
T = int(input())

for t in range(T):
    a = input()
    bin = ""
    for i in a:
        if i.isalpha():
            if i in ["a", "e", "i", "o", "u"]:
                bin += "0"
            else:
                bin += "1"
    print(int(bin, 2) % 1000000007)
