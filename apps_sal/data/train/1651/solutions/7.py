def solution(args):
    (temp, segments) = (list(), list())
    while args:
        temp.append(args.pop(0))
        if len(args) != 0 and temp[-1] == args[0] - 1:
            continue
        if len(temp) <= 2:
            segments += temp
        else:
            segments.append(f'{temp[0]}-{temp[-1]}')
        temp = []
    return ','.join((str(s) for s in segments))
