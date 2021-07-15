#Goal:
# Fix Jenny's function so that it returns a standard greeting for any arbitrary user, but returns a special greeting for
# her crush Johnny.
#General Strategy:
# When Python processes Jenny's code it will always return the first greeting even if the input name is Johnny.
# The problem is that Johnny is receiving both greetings when Jenny only wants him to receive the bottom greeting.
# The way to solve this problem is to create an if statement for Johnny and an else statement for all other users.

def greet(name):
    # Here is the if statement so that if the user is Johnny, then the special message is returned.
    if name == "Johnny":
        return "Hello, my love!"
    # Here is the else statement which returns the standard greeting for any user aside from Johnny.
    else:
        # Here format is used to replace the name inside brackets within the string, with the input/variable 'name'
        # from the definition of the function.
        return "Hello, {name}!".format(name=name)

