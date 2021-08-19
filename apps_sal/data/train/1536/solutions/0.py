test_cases = int(input())
for i in range(test_cases):
    no_of_elements = int(input())
    sequence = list(map(int, input().split()))
    d1 = sequence[1] - sequence[0]
    d2 = sequence[2] - sequence[1]
    d3 = (sequence[3] - sequence[0]) / 3
    d4 = (sequence[3] - sequence[1]) / 2
    d5 = (sequence[2] - sequence[0]) / 2
    if d2 == d4:
        d = d2
    elif d3 == d5:
        d = d3
    elif d1 == d3:
        d = d1
    elif d1 == d5:
        d = d1
    if d == d1:
        for i in range(no_of_elements):
            sequence[i] = int(sequence[0] + i * d)
    else:
        for i in range(no_of_elements):
            sequence[i] = int(sequence[-1] - (no_of_elements - i - 1) * d)
    for i in sequence:
        print(i, end=' ')
    print('\n')
