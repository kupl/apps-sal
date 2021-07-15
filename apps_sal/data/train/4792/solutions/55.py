parse_float = lambda string: None if not all(c.isdigit() or c=='.' for c in string) else float(string)
