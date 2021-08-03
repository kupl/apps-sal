import itertools as it


def iter_len(iterator):
    return len(list(iterator))


def window(iterable, length):
    iterators = [it.islice(iterator, idx, None) for idx, iterator in enumerate(it.tee(iterable, length))]
    return zip(*iterators)


def replace_zero(arr):

    def accumulate_group(total, group):
        _, prev_length, prev_begin = total
        key, length, _ = group
        return key, length, prev_begin + prev_length

    groups = ((key, iter_len(group), 0) for key, group in it.groupby(arr))
    empty = [(None, 0, 0)]
    indexed_groups = it.accumulate(it.chain(empty, groups, empty), accumulate_group)

    def is_zero(group): return group[0] == 0
    def is_one(group): return group[0] == 1
    def group_len(group): return group[1]
    def first_pos(group): return group[2]
    def last_pos(group): return group[2] + group[1] - 1
    def revelant(triple): return is_zero(triple[1])

    triples = filter(revelant, window(indexed_groups, 3))

    def solutions(triples):
        for left, this, right in triples:
            if group_len(this) == 1:
                yield group_len(left) + 1 + group_len(right), first_pos(this)
            else:
                yield group_len(left) + 1, first_pos(this)
                yield group_len(right) + 1, last_pos(this)

    length, positions = max(solutions(triples))
    return positions
