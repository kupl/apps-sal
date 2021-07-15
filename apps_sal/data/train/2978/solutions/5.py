from collections import Counter

def count_sel(lst):
    freq = Counter(lst)
    return [len(lst),len(set(lst)),len([x for x in lst if lst.count(x) == 1]),[sorted(k for k,v in list(freq.items()) if v == freq[max(freq, key=freq.get)]), freq[max(freq, key=freq.get)]]]

