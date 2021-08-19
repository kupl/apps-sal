for i in range(int(input())):
    n = int(input())
    lens = len(str(bin(n))) - 2
    # print(lens)
    if(str(bin(n)).count('1') == 1):
        lens -= 1
    print(1 << lens)
    # print()
