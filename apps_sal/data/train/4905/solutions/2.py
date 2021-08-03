# 09/01/2019
# I did all the work in the Sample Test section, then after submitting my answer, all of my work in the Sample Test section is gone.
# So I'm doing this over and will incude my test data here as so it does not vanish when submitting the work.
# I think from now on I will use my local machine so I don't loose all of my testing steps and have to do it all over again.

def answer(puzzlebox):
    # Print statements are your friend.
    return(42)

# *** Below is the test dataand process I used to figure out that returning then number 42 is the the solution to the challenge ***


# Printing attributes of puzzlebox
print((dir(puzzlebox)))  # Returns the puzzlebox object attributes
print((list(dir(puzzlebox))[25:30]))  # prints attributes with values from puzzlebox [answer, hint, hint_two, key, lock]

# See values assigned to the puzzlebox object
print((puzzlebox.answer))      # returns "Ha, not quite that easy."
print((puzzlebox.hint))        # returns "How do you normally unlock things?
print((puzzlebox.hint_two))    # returns "The lock attribute is a method.  Have you called it with anything yet? "
print((puzzlebox.key))         # returns "50", but running code again returns "78", then "57", so key is a random number
print((puzzlebox.lock))        # returns "<bound method Puzzlebox.lock of The built-in dir() function is useful.
# Continue adding print statements till you know the answer.>

# Try passing stuff to the lock function as suggested by hint_two
num = 2
float = 2.3
bool = False
str = "hello"

print((puzzlebox.lock(num)))             # returns "Did you know the key changes each time you print it?"
print((puzzlebox.lock(float)))           # returns "This method expects an integer."
print((puzzlebox.lock(bool)))            # return  "This method expects an integer."
print((puzzlebox.lock(str)))             # returns "This method expects an integer."
print((puzzlebox.lock(puzzlebox.key)))   # returns "You put the key in the lock! The answer is, of course, 42.
# Return that number from your answer() function to pass this kata."
# HOORAY!  Just return the number 42!
