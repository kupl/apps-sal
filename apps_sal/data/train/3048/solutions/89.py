def alternateCase(s):
    final_ans = ""
    tokens = [c for c in s]
    for c in tokens:
        if c.isupper():
            final_ans = final_ans + c.lower()
        else:
            final_ans = final_ans + c.upper()
    return final_ans
