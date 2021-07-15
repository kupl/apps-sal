def dist_from_prev_a(x):
    return ord(x)-ord('a')+1

def encode(message, key):
    x=[dist_from_prev_a(i) for i in message]
    y=list(str(key)*len(message))[:len(message)]
    return [x[i]+int(y[i]) for i in range(len(x))]

