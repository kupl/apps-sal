def unused_digits(*ints):
    return ''.join(sorted(list(set('0123456789') - set((c for i in ints for c in str(i))))))
