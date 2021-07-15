def linux_type(s):
    return {x: y for x, y in zip("-dlcbpsD", "file directory symlink character_file block_file pipe socket door".split(" "))}[s[0]]
