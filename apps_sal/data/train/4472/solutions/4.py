def bear_fur(bears):
    bears = "".join(bears)
    dict = {
        'blackblack' : 'black',
        'brownbrown' : 'brown',
        'whitewhite' : 'white',
        'brownblack' : 'dark brown',
        'blackbrown' : 'dark brown',
        'blackwhite' : 'grey',
        'whiteblack' : 'grey',
        'brownwhite' : 'light brown',
        'whitebrown' : 'light brown'
    }
    return dict.get(bears, 'unknown')
