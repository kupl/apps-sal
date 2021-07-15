split0 = lambda x: [x] if x&1 else [(x>>1) - ((x&2)>>1^1), (x>>1) + ((x&2)>>1^1)]
split1 = lambda x: [x] if x&1 else [1, x-1]
split2 = lambda x: [x] if x&1 else split2(x>>1)*2
split3 = lambda x: [x] if x&1 else [1]*x

splits = (split0, split1, split2, split3)

def split_all_even_numbers(numbers, way):
    return [y for x in numbers for y in splits[way](x)]
