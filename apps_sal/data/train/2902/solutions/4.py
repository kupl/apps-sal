def opposite(number):
    """
    Function have one required argument.
    At start our function check your number. If it's int, float or complex - func multiplies number by -1 and return it
    If our argument is string, try to convert to complex number
    If we had Value Error in our convertation, say(use print when except):
        Input data cannot be represented as a number.
    And after return None

    Return:
        Number int or float if input number is int or float.
        Number complex if input number is complex or wrote in string
        None if we had empty line or another input types
    """
    if type(number) is int or type(number) is float or type(number) is complex:
        number = number * -1
        return number
    else:
        try:
            number = complex(number) * -1
            return number
        except ValueError:
            print('Input data cannot be represented as a number')
            return None
