def words_to_object(s):
    s = s.split()
    arr = [{'name': i, 'id': j} for (i, j) in zip(s[::2], s[1::2])]
    return str(arr).replace("'name':", 'name :').replace("'id':", 'id :')
