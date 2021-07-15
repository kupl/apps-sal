from collections import Counter
def create_anagram(s,t):
    c_s,c_t=Counter(s),Counter(t)
    return min(sum((c_s-c_t).values()),sum((c_t-c_s).values()))
