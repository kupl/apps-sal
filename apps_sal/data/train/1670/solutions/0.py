import sys


def main():
    s = sys.stdin.readline
    save = {' ': '%20', '!': '%21', '$': '%24', '%': '%25', '(': '%28', ')': '%29', '*': '%2a'}
    string = s().strip()
    while True:
        output = []
        if '
        return
        for i in string:
            if i in save:
                output.append(save[i])
            else:
                output.append(i)
        print(''.join(output))
        string = s().strip()


def __starting_point():
    main()


__starting_point()
