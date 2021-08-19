# -*- coding: utf-8 -*-
def heavy_metal_umlauts(boring_text):
    a = 'AOaoEUeuIYiy'
    b = 'ÄÖäöËÜëüÏŸïÿ'
    return boring_text.translate(str.maketrans(a, b))
