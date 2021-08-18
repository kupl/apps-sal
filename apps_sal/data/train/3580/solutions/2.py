def get_positions(n):
    num2 = n
    num3 = n
    p2 = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    p3 = [0, 0, 0, 0, 0, 0, 0, 0, 0,
          1, 1, 1, 1, 1, 1, 1, 1, 1,
          2, 2, 2, 2, 2, 2, 2, 2, 2]

    while num2 >= 9:
        num2 = num2 % 9
    n2 = p2[num2]

    while num3 >= 27:
        num3 = num3 % 27
    n3 = p3[num3]

    return (n % 3, n2, n3)
