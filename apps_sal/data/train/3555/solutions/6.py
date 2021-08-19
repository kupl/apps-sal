def Hanoi_Solution(n):
    if n == 0:
        return [[], [], []]
    if n == 1:
        return [[[1], [], []], [[], [], [1]]]
    else:
        L = len(Hanoi_Solution(n - 1))
        first_half = Hanoi_Solution(n - 1)
        for i in range(L):
            first_half[i][0].insert(0, n)
            temp_1 = first_half[i][2]
            first_half[i][2] = first_half[i][1]
            first_half[i][1] = temp_1
        second_half = Hanoi_Solution(n - 1)
        for i in range(L):
            second_half[i][2].insert(0, n)
            temp_2 = second_half[i][1]
            second_half[i][1] = second_half[i][0]
            second_half[i][0] = temp_2
        for i in second_half:
            first_half.append(i)
        return first_half


def hanoiArray(n):
    return ''.join((str(i) + '\n' for i in Hanoi_Solution(n)))[:-1]
