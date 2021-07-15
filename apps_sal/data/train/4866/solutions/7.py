ways = {
    0 : lambda n : [n//2]*2 if (n//2)%2 else [n//2-1,n//2+1],
    1 : lambda n : [1,n-1],
    2 : lambda n : [ [n//x]*x for x in range(2,n+1) if sum([n//x]*x)==n and (n//x)%2][0],
    3 : lambda n : [1]*n
}

def split_all_even_numbers(numbers, way):
  return [x for lists in [ways[way](x) if not x%2 else [x] for x in numbers] for x in lists]
