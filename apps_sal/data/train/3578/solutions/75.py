#this function tells you how much paper you need based on the how many people their are and how many pages their are.
def paperwork(people, pages):
    blank=people*pages
    if people<0:
        blank=0
    if pages<0:
        blank=0
    return blank
