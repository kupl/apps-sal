def main():
    from sys import stdin, stdout
    input1 = stdin.readline
    print1 = stdout.write
    for _ in range(int(input1())):
        input1()
        t = tuple(map(int, input1().rstrip('\n')))
        for mid in range(10):
            ans = []
            lasts = [0, 0, 0]
            lasts[2] = mid
            for ti in t:
                if ti < lasts[1]:
                    break
                if ti < lasts[2]:
                    color = 1
                else:
                    color = 2
                ans.append(str(color))
                lasts[color] = ti
            else:
                if lasts[1] == mid:
                    print1(''.join(ans) + '\n')
                    break
        else:
            print1('-\n')


main()
