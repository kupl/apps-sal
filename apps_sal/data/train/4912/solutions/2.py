import re


def html_end_tag_by_start_tag(start_tag):
    return re.sub('<(\\w+)(?:.*)>', '</\\1>', start_tag)
