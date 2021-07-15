from re import search
is_digit = lambda n : bool(search(r"(^[0-9]$)(?!\s)", n))
