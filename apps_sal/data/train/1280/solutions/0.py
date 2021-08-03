t = int(input())
for _ in range(t):
    xyz = input().strip()

    string = 0

    for i in range(len(xyz) // 2):
        string = string + (abs(ord(xyz[i]) - ord(xyz[len(xyz) - i - 1])))

    print(string)
