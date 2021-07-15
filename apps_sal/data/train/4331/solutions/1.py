# -*- coding: utf-8 -*-
def heavy_metal_umlauts(boring_text):
    return boring_text.translate(str.maketrans('AEIOUYaeiouy','ÄËÏÖÜŸäëïöüÿ'))
