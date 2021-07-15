def rgb(r, g, b):
    """
    Return hex string representation of ``r,g,b`` values. A saturation \
will be applied to the input values to ensure they are betweem 0 \
and 255.
    
    :param r: Red channel
    :type r: int 
    
    :param g: Green channel
    :type g: int 
    
    :param b: Blue channel
    :type b: int 
    
    :return: Hex representation.
    :rtype: str
    
    >>> rgb(123,45,67)
    '7B2D43'
    >>> rgb(-20,123,456)
    '007BFF'
    >>> rgb('no int',123,123)
    Traceback (most recent call last):
        ...
    TypeError: 'r' is not of type int
    >>> rgb(123,'no int',123)
    Traceback (most recent call last):
        ...
    TypeError: 'g' is not of type int
    >>> rgb(123,123,'no int')
    Traceback (most recent call last):
        ...
    TypeError: 'b' is not of type int
    """
    
    if not type(r).__name__ == 'int':    # python2 does not have instanceof()
        raise TypeError("'r' is not of type int")
    if not type(g).__name__ == 'int':    # python2 does not have instanceof()
        raise TypeError("'g' is not of type int")
    if not type(b).__name__ == 'int':    # python2 does not have instanceof()
        raise TypeError("'b' is not of type int")
    
    return "{r:02X}{g:02X}{b:02X}".format(
        r=saturate(r),
        g=saturate(g),
        b=saturate(b),
    )


def saturate(x):
    """
    Saturates an integer ``x`` to be ``0<=x<=255``.
    
    :param x: Integer to be saturated
    :type x: int 
    
    :return: Saturated integer
    :rtype: int
    
    >>> saturate(345)
    255
    >>> saturate(-3)
    0
    >>> saturate(123)
    123
    >>> saturate("no int")
    Traceback (most recent call last):
        ...
    TypeError: given value is not of type int
    """
    if not type(x).__name__ == 'int':    # python2 does not have instanceof()
        raise TypeError("given value is not of type int")
    
    x = 0 if x<0 else x
    x = 255 if x>255 else x
    
    return x


def __starting_point():
    import doctest
    doctest.testmod()
__starting_point()
