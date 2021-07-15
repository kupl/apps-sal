def likes(names):
    if not names:
        return "no one likes this"
    size = len(names)
    if size == 1:
        return "%s likes this" % names[0]
    if size == 2:
        return "%s and %s like this" % (names[0], names[1])
    if size == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    if size >= 4:
        return "%s, %s and %s others like this" % (names[0], names[1], len(names[2:]))
