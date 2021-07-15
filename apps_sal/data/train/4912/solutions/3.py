def html_end_tag_by_start_tag(s):
    return '</{}>'.format(s[1:s.find(' ')])
