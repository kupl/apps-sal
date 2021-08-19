import sys

input_methods = ['clipboard', 'file', 'key']
using_method = 0
input_method = input_methods[using_method]


def tin(): return map(int, input().split())
def lin(): return list(tin())


mod = 1000000007

# +++++


def main():
    #a = int(input())
    n, a, b = tin()
    #s = input()
    al = lin()
    pos = al[0]
    ret = 0
    for np in al[1:]:
        ret += min(b, (np - pos) * a)
        pos = np
    return ret


# +++++
isTest = False


def pa(v):
    if isTest:
        print(v)


def input_clipboard():
    import clipboard
    input_text = clipboard.get()
    input_l = input_text.splitlines()
    for l in input_l:
        yield l


def __starting_point():
    if sys.platform == 'ios':
        if input_method == input_methods[0]:
            ic = input_clipboard()
            def input(): return ic.__next__()
        elif input_method == input_methods[1]:
            sys.stdin = open('inputFile.txt')
        else:
            pass
        isTest = True
    else:
        pass
        #input = sys.stdin.readline

    ret = main()
    if ret is not None:
        print(ret)


__starting_point()
