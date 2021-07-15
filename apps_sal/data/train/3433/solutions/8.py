import itertools as it

def iter_len(iterator):
    return len(list(iterator))

def window (iterable, length):
    iterators = [it.islice(iterator, idx, None) for idx,iterator in enumerate(it.tee(iterable, length))]
    return zip(*iterators)
    
def replace_zero(arr):

    def accumulate_group(total, group):
        _, prev_length, prev_begin = total 
        key, length, _ = group
        return key, length, prev_begin+prev_length
        
        
    groups = ((key, iter_len(group), 0) for key, group in it.groupby(arr))
    empty = [(None, 0, 0)]
    indexed_groups = it.accumulate(it.chain(empty,groups,empty), accumulate_group)
    
    is_zero = lambda group: group[0] == 0
    is_one = lambda group: group[0] == 1
    group_len = lambda group: group[1]
    first_pos = lambda group: group[2]
    last_pos = lambda group: group[2] + group[1] - 1
    revelant = lambda triple: is_zero(triple[1])
        
    triples = filter(revelant, window(indexed_groups,3))
    
    def solutions (triples): 
        for left,this,right in triples:
            if group_len(this) == 1:
                yield group_len(left)+1+group_len(right), first_pos(this)
            else:
                yield group_len(left)+1, first_pos(this)
                yield group_len(right)+1, last_pos(this)
    
    length, positions = max(solutions(triples))
    return positions
