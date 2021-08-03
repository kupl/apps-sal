def to_alternating_case(string):
    def alter_case(let): return let.lower() if let.isupper() else let.upper()
    return ''.join(map(alter_case, string))
