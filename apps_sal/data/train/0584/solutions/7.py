def solve(S):
    if S[0] == '0':
        return 0
    count = 0
    flag = False
    for char in S:
        if char == '0':
            count += 1
            flag = True
        elif char == '1' and (not flag):
            continue
        elif char == '1' and flag:
            break
    return count


def main():
    N = int(input())
    for case in range(N):
        S = input()
        print(solve(S))
    return


def __starting_point():
    main()


__starting_point()
