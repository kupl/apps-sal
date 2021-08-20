(_, _, *S) = open(0).read().split()
print(''.join(sorted(S)))
