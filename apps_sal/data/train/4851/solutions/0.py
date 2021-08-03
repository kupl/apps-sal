from distutils.version import LooseVersion


def sort_ranks(ranks):
    return sorted(ranks, key=LooseVersion)
