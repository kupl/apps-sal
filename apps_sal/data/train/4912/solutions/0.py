def html_end_tag_by_start_tag(start_tag):
    return '</' + start_tag[1:-1].split(' ')[0] + '>'
