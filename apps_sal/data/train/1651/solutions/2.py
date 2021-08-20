def solution(args):
    result = ''
    i = 0
    while i < len(args):
        val = args[i]
        while i + 1 < len(args) and args[i] + 1 == args[i + 1]:
            i += 1
        if val == args[i]:
            result += ',%s' % val
        elif val + 1 == args[i]:
            result += ',%s,%s' % (val, args[i])
        else:
            result += ',%s-%s' % (val, args[i])
        i += 1
    return result.lstrip(',')
