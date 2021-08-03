# cook your dish here
for i in range(int(input())):
    n = int(input())
    count = 0
    colours = input()
    for j in range(1, n):
        if colours[j] == colours[j - 1]:
            count += 1

    print(count)
