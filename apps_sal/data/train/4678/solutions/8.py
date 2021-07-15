from collections import Counter
def find_the_missing_tree(trees):
    c=Counter(trees)
    odd=[k for k,v in c.items() if v%2]
    even=[k for k,v in c.items() if v%2==0]
    return even[0] if len(even)==1 else odd[0]
