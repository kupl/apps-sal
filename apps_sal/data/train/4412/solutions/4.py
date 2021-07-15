# Partition generator taken from 
# https://stackoverflow.com/questions/19368375/set-partitions-in-python
def partition(collection):
    if len(collection) == 1:
        yield [ collection ]
        return

    first = collection[0]
    for smaller in partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:]
        # put `first` in its own subset 
        yield [ [ first ] ] + smaller
        
def part_sum(part_list):
    tot_sum = 0
    for elem in part_list:
        tot_sum += sum(int(''.join(x)) for x in elem)
    return tot_sum

def find(n,z):
    min_sum = part_sum([x for x in partition(list(str(n)))][1:]) + z
    i = 1
    nf_sum = part_sum([x for x in partition(list(str(n+i)))][1:])
    while nf_sum <= min_sum:
        i += 1
        nf_sum = part_sum([x for x in partition(list(str(n+i)))][1:])
    return n+i
