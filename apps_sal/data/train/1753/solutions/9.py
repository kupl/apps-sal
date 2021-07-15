from math import floor, ceil

def least_bribes(bribes):
    bribes_len = len(bribes)
    halfway = (bribes_len - 1) / 2
    solved_bribes = set()
    bribe_dict = {}
    part_stack = [(0, bribes_len, floor(halfway), ceil(halfway))]
    while part_stack:
        start, end, left, right = part_stack.pop()
        
        if (start, end) in solved_bribes:
            continue
        
        width = end - start
        if width <= 2:
            bribe_dict[(start, end)] = sum(bribes[start:end])
            solved_bribes.add((start, end))
            continue
        if width == 3:
            bribe_dict[(start, end)] = bribes[start + 1] + max(bribes[start:end:2])
            solved_bribes.add((start, end))
            continue
        
        new_bribe = None
        missing_bribes = False
        for pivot in (left, right):
            neighbor_bribes = [0, 0]
            for n_i, n_start, n_end in ((0, start, pivot), (1, pivot + 1, end)):
                if (n_start, n_end) in bribe_dict:
                    neighbor_bribes[n_i] = bribe_dict[(n_start, n_end)]
                else:
                    halfway = n_start + (n_end - n_start - 1) / 2
                    if not missing_bribes:
                        part_stack.append((start, end, left, right))
                        missing_bribes = True
                    part_stack.append((n_start, n_end, floor(halfway), ceil(halfway)))
            if missing_bribes:
                continue
            bribe_total = bribes[pivot] + max(bribe_dict[(start, pivot)], bribe_dict[(pivot + 1, end)])
            if not new_bribe or bribe_total < new_bribe:
                new_bribe = bribe_total
        
        if missing_bribes:
            continue
        
        if (start, end) not in bribe_dict or new_bribe < bribe_dict[(start, end)]:
            bribe_dict[(start, end)] = new_bribe
        if left > start:
            part_stack.append((start, end, left - 1, right + 1))
            continue
            
        solved_bribes.add((start, end))
        
    return bribe_dict[(0, bribes_len)]
