import sys
3


def main():
    n = int(input())
    home = input().strip()

    cnt_fr, cnt_to = 0, 0
    for i in range(n):
        fr, to = input().strip().split('->')
        if fr == home:
            cnt_fr += 1
        if to == home:
            cnt_to += 1

    if cnt_fr == cnt_to + 1:
        print("contest")
    elif cnt_fr == cnt_to:
        print("home")
    else:
        return(1)


main()
