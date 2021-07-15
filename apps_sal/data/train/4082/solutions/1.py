TYPE_SEQ = {(1,): 1, (0,1): 2, (-1,):3, (-1,0): 4, (0,): 5}

def sequence_classifier(arr):
    countSet = { (a<b) - (a>b) for a,b in zip(arr, arr[1:]) }
    return TYPE_SEQ.get(tuple(sorted(countSet)), 0)
