def who_is_paying(name):
    return sorted(set([name, name[:2]]), reverse=True)
