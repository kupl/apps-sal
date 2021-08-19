for i in range(int(input())):
    L = list(map(int, input().split()))
    if 2 ** 0.5 * L[0] / L[1] < 2 * (L[0] / L[2]):
        print('Stairs')
    else:
        print('Elevator')
