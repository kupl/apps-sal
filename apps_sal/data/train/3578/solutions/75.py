def paperwork(people, pages):
    blank = people * pages
    if people < 0:
        blank = 0
    if pages < 0:
        blank = 0
    return blank
