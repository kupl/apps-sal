closest_sum=lambda a,n:min(map(sum,__import__('itertools').combinations(a,3)),key=lambda c:abs(c-n))
