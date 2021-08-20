import re


def near_flatten(nested):
    nested = str(nested)
    flatten_regex = re.compile('\\[+(\\d+)(?:, )?(\\d+)?(?:, )?(\\d+)?(?:, )?(\\d+)?\\]+')
    matches = flatten_regex.finditer(nested)
    fixed_ls = [flatten_regex.sub('\\1 \\2 \\3 \\4', i.group()).split() for i in matches]
    fixed_ls = [[int(x) for x in i] for i in fixed_ls]
    return sorted(fixed_ls)
