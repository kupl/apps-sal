# Goal: Create a function that will return true if the string is a single integer or float.
# If this condition is not met, then return False.

# function name that checks if the string entered is a digit
def isDigit(string):
    # try is used to test this piece of code for errors. It is effectively testing to see if it is true/will run.
    try:
        # apparently float will also work if the string entered is a digit. Float works for both decimals and integers.
        float(string)
        return True
    # except will make an exception when receiving a value error, in this case the string isn't a float, and will return
    # False.
    except ValueError:
        return False
