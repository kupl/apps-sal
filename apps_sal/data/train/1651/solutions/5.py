""" noob solution, explained for noobs :) """


def printable(arr):
    return (','.join(str(x) for x in arr) if len(arr) < 3
            else f'{arr[0]}-{arr[-1]}')


def solution(args):
    chunk, ret = [], []

    for i in args:
        if not len(chunk) or i == chunk[-1] + 1:
            chunk.append(i)
        else:
            ret.append(printable(chunk))
            chunk = [i]

    ret.append(printable(chunk))

    return ','.join(ret)
