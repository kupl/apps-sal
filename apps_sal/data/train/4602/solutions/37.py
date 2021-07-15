import collections
def is_anagram(test, original):
    return collections.Counter([i.lower() for i in sorted(test)]) ==  collections.Counter([i.lower() for i in sorted(original)])
