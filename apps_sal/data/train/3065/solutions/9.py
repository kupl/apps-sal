from re import finditer


def get_textliterals(pv_code):
    l = len(pv_code)
    pv_code = pv_code.replace("''", '""')
    addedQuote = False
    if not pv_code.endswith("'"):
        addedQuote = True
        pv_code += "'"
    patterns = ['/\\*(?:\\n|.)*?\\*/', '--.+', "'(?:\n|.)*?'"]
    comments = [m.span() for m in finditer(patterns[0], pv_code)] + [m.span() for m in finditer(patterns[1], pv_code)]
    answer = []
    candidates = [m.span() for m in finditer(patterns[2], pv_code)]
    for (startA, endA) in candidates:
        ok = True
        for (startB, endB) in comments:
            if startB < startA < endA < endB:
                ok = False
                break
        if ok:
            if addedQuote and endA - 1 == l:
                endA -= 1
            answer.append((startA, endA))
    return answer
