import re


def html_end_tag_by_start_tag(s):
    r = re.match('<\\w+', s).group()
    return f'</{r[1:]}>'
