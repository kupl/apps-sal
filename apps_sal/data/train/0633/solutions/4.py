for _ in range(int(input())):
    no_inpt = int(input())
    height_mn = []
    for _ in range(no_inpt):
        height_mn.append(int(input()))
    height_mn.sort()
    print(max(height_mn))
