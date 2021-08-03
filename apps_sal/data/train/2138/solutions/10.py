a = list(input())
b = list(input())

print(['NO', 'YES'][a.count('1') + a.count('1') % 2 >= b.count('1')])
