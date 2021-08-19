def get_middle(s):
    if len(s) % 2 == 0:
        iA = int((len(s) / 2) - 1)
        iB = int((len(s) / 2) + 1)
        return s[iA:iB]  # Remeber indexing starts at 0 and iB is not included, hence +/- 1 above
    else:
        return s[int(len(s) / 2)]  # int makes sure its integer, and rounds down to correct index
