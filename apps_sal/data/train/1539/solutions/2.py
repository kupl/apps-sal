T = int(input())
for i in range(1, T + 1):
    J = input()
    S = input()
    count = 0
    for letter in S:
        if letter in J:
            count += 1
    print(count)
