import collections
def char_freq(message):
    hashing = collections.defaultdict(int)
    for i in message:
        hashing[i]+=1
    return hashing
    

