def friend(x):
    myFriends = []                   # Initialize list variable
    for person in x:                 # Loop through list of names
        if len(person) == 4:         # Check to see if the name is of length 4
            myFriends.append(person)  # If the name is 4 characters long, append it to variable myFriends
    return myFriends                 # Return myFriends list
