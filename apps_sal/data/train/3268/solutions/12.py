def words_to_object(s):
    s = s.split()
    return "[" + ", ".join(f"{{name : '{s[i]}', id : '{s[i+1]}'}}" for i in range(0, len(s), 2)) + "]"
