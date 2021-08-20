def main():
    from sys import stdin, stdout
    ans = []
    stdin.readline()
    for new_s in map(int, stdin.readline().split()):
        new_c = 1
        while ans and new_s * ans[-1][1] <= ans[-1][0] * new_c:
            (old_s, old_c) = ans.pop()
            new_s += old_s
            new_c += old_c
        ans.append((new_s, new_c))
    for (s, c) in ans:
        stdout.write(f'{s / c}\n' * c)


main()
