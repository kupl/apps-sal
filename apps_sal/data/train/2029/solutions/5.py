n = int(input())

if n % 2 == 0:
    print('NO')

else:
    first_half = [1]
    second_half = [2]

    for i in range(n - 1):
        first_half.append((first_half[i] + 3) if i % 2 == 0 else (first_half[i] + 1))
        second_half.append((second_half[i] + 1) if i % 2 == 0 else (second_half[i] + 3))

    print('YES')
    print(*(first_half + second_half))
