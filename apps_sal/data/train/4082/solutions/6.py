def sequence_classifier(arr):
    a, l, l_ = sorted(arr), len(arr), len(set(arr))
    return [[0,[[3,4][arr==a[::-1] and l_!=l],[1,2][arr==a and l_!=l]][arr==a]][arr in [a,a[::-1]]],5][l_==1]
