from math import ceil
def wallpaper(l, w, h):
    numarr = ['zero','one','two','three','four','five','six','seven','eight','nine', 'ten', 'eleven',
              'twelve','thirteen','fourteen','fifteen','sixteen', 'seventeen','eighteen','nineteen', 'twenty']
    return numarr[ceil(l and w and ((l + w) * h * 2 * 1.15) / 5.2)]

