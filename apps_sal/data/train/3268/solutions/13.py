def words_to_object(s):
    return'[' + ', '.join(f"{{name : '{a}', id : '{b}'}}"for a, b in zip(*[iter(s.split())] * 2)) + ']'
