import re


def magic_call_depth_number(pattern):
    subroutines = {}  # list them by number
    s = re.compile(r'p(\d+)((P\d+|[FLR]*\d*)+)q')
    subrout = s.search(pattern)
    while subrout:
        # put the subroutine in the dictionary
        subroutines["P" + subrout.group(1)] = tokens(subrout.group(2))
        # extract this subroutine from the pattern and see if there are more
        pattern = pattern.replace(subrout.group(0), "")
        subrout = s.search(pattern)
    # Make a tree
    depths = walk_tree(tokens(pattern), [], subroutines)
    return [min(depths), max(depths)]


def tokens(pattern):
    return re.findall(r'([PFLR]\d*)', pattern)


def walk_tree(token_list, stack, subroutine_dict):
    depths = []
    stops_here = True
    for t in token_list:
        if t.startswith("P"):
            stops_here = False
            if t in stack:
                depths.append(len(stack))
            else:
                depths.extend(walk_tree(subroutine_dict[t], stack + [t], subroutine_dict))
    if stops_here:
        depths.append(0)
    return depths
