def get_textliterals(pv_code):
    literal_start = -1
    result = []
    comment = False
    inline_comment = False
    quote = False
    for idx, c in enumerate(pv_code):

        if idx + 1 == len(pv_code) and literal_start != -1:
            literal_end = idx + 1
            result.append((literal_start, literal_end))
            break
        elif c == '*' and pv_code[idx - 1] == '/':
            comment = True
        elif c == '/' and pv_code[idx -1] == '*' and comment:
            comment = False
        elif c == "'" and literal_start != -1 and not comment and not inline_comment:
            if idx+1 < len(pv_code) and pv_code[idx+1] == "'":
                quote = True
            elif pv_code[idx-1] == "'":
                continue
            else:
                literal_end = idx + 1
                result.append((literal_start, literal_end))
                literal_start = -1
                quote = False
        elif c == "'" and quote == False and not comment and not inline_comment:
            literal_start = idx
        elif c == '-' and pv_code[idx-1] == '-':
            inline_comment = True
        elif c == '\n':
            inline_comment = False
    return result
