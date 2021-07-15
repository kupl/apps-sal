def html_end_tag_by_start_tag(start_tag):
    w = start_tag.strip('< >').split(' ')
    return '</{}>'.format(w[0])
