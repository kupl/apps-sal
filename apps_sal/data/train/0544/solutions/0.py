# cook your dish here
def decode(L, S):
    str_2 = ""
    lst = []
    for i in range(L // 4):
        str_1 = "abcdefghijklmnop"
        S_1 = S[(i * 4):(4 * (i + 1))]
        for j in range(4):
            if(S_1[j] == "1"):
                str_1 = str_1[len(str_1) // 2:len(str_1)]
            else:
                str_1 = str_1[0:len(str_1) // 2]
        str_2 = str_2 + str_1
    print(str_2)


T = int(input())
for i in range(T):
    L = int(input())
    S = input()
    decode(L, S)
