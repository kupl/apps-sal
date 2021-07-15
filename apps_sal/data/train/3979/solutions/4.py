def match_arrays(v, r):
    tool = lambda x: {tuple(y) if type(y) == list else y for y in x}
    return len(tool(v) & tool(r))

# DON'T remove
verbose = False # set to True to diplay arrays being tested in the random tests
