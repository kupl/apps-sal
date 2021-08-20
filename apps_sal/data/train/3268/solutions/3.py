def words_to_object(s):
    return '[' + ', '.join((f"{{name : '{a}', id : '{b}'}}" for (a, b) in zip(s.split()[::2], s.split()[1::2]))) + ']'
