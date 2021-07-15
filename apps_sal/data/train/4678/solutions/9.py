import collections

def find_the_missing_tree(trees):
    count = collections.Counter( trees )
    return min( count, key = count.get )

