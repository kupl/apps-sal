from copy import deepcopy


def word_problem(rules: List[Tuple[str, str]], from_str: str, to_str: str, applications: int) -> bool:
    if applications == 0 or from_str == to_str:
        return from_str == to_str
    currentStrings = [from_str]
    for i in range(applications):
        # create all possible next strings from current string(s), using all rules
        nextStrings = []
        # iterate over all current strings
        for s in currentStrings:
            # determine all possible next strings
            for rule in rules:
                pos = 0
                while pos < len(s) and rule[0] in s[pos:]:
                    if s[pos:].startswith(rule[0]):
                        newString = s[:pos] + rule[1] + s[pos + len(rule[0]):]
                        if newString == to_str:
                            return True
                        if not newString in nextStrings:
                            nextStrings.append(newString)
                    pos += 1
        currentStrings = nextStrings
    return False
