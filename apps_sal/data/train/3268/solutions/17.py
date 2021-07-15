def words_to_object(s):
    a=s.split(' ')
    r=[]
    for name,_id in zip(a[::2],a[1::2]):
        r.append("{{name : '{}', id : '{}'}}".format(name,_id))
    return '[{}]'.format(', '.join(r))
