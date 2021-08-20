def wallpaper(l, w, h):
    dict = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
    rolls = int((l + w) * 2 * h / 0.52 / 10 * 1.15) + 1 if l and w and h else 0
    return dict[rolls]
