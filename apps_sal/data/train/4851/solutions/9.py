import re


def sort_ranks(ranks):
    return sorted(ranks, key=lambda x: float(re.sub("(?<=\.\d)(\.)", "", x)))
