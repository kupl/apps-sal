for j in range(int(input())):
    m, n = list(map(int, input().split()))
    X, Y = list(map(int, input().split()))
    l = int(input())
    s = input()
    x = 0
    y = 0
    for i in s:

        if i == 'L':
            x = x - 1
        elif i == 'R':
            x = x + 1
        elif i == 'U':
            y = y + 1
        else:
            y = y - 1
    if x == X and y == Y:
        print(f'Case {j+1}: REACHED')
    elif x > m or x < 0 or y < 0 or y > n:
        print(f'Case {j+1}: DANGER')
    else:
        print(f"Case {j+1}: SOMEWHERE")
    # Case 1: REACHED
# Case 2: DANGER
