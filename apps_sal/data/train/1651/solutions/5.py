""" noob solution, explained for noobs :) """


def printable(arr):
    return (','.join(str(x) for x in arr) if len(arr) < 3  # one or two consecutive integers : comma separated
            else f'{arr[0]}-{arr[-1]}')                    # more : dash separated first and last integer


def solution(args):
    chunk, ret = [], []                                    # instantiate variables

    for i in args:                                         # for each integer
        if not len(chunk) or i == chunk[-1] + 1:  # if first or consecutive
            chunk.append(i)  # add to current chunk
        else:  # else, it's a gap
            ret.append(printable(chunk))  # save current chunk
            chunk = [i]  # and restart a new one

    ret.append(printable(chunk))                           # do not forget last chunk !

    return ','.join(ret)                                   # return comma separated chunks
