from collections import OrderedDict


def common_ground(s1, s2):
    s3 = []
    [s3.append(i) for i in s2.split() if i in s1.split()]

    if len(s3) == 0:
        return 'death'
    else:
        return ' '.join(OrderedDict.fromkeys(s3))
