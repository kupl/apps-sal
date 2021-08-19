def feast(beast, dish):
    # your code here

    if beast[-1].lower() == dish[-1].lower() and beast[0].lower() == dish[0].lower():
        return True
    else:
        return False
