def html_end_tag_by_start_tag(s):
    result = s.split()[0][0]+'/'+s.split()[0][1:]+ '>'
    if result[-2:] == '>>':
        result = result.replace('>>','>')
    return result
