def match_arrays(v, r):

    def tool(x):
        return {tuple(y) if type(y) == list else y for y in x}
    return len(tool(v) & tool(r))


verbose = False
