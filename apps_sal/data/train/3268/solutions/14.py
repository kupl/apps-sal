def words_to_object(s):
    nis = s.split()
    dicts_list = [{'name': name, 'id': id} for (name, id) in zip(nis[::2], nis[1::2])]
    return f'{dicts_list}'.replace("'name'", 'name ').replace("'id'", 'id ')
