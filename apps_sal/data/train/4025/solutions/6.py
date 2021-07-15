def func(l):
    a=int(sum(l)/len(l))
    return [a,'{:b}'.format(a),'{:o}'.format(a),'{:x}'.format(a)]
