decode=lambda s:''.join(chr(219-ord(c)-155*(c<'a'))for c in s)
