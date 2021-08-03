def parse_float(string): return None if not all(c.isdigit() or c == '.' for c in string) else float(string)
