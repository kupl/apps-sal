print_nums = lambda*a: '\n'.join('%0*d' % (len(str(max(a))), n)for n in a)
