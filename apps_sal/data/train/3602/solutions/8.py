from re import findall


def run_length_encoding(string):
    return [[len(a), b] for a, b in findall(r"((.)\2*)", string)]

    #match_runs = r"((.)\2*)"
    #runs = findall(match_runs, string)
    # return [[len(run), char] for run, char in runs]
