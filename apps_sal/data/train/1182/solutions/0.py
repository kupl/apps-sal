def interesting_nums(m):
    nums = []
    for x in range(m + 1, 2 * m + 1):
        if x * m % (x - m) == 0:
            nums.append(x)
    return nums


def main():
    T = int(input())
    for _ in range(T):
        num_list = interesting_nums(int(input()))
        print(len(num_list))
        for num in num_list:
            print(num)


main()
