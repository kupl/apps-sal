#input - two strings
#ouput - boolean
#edge cases - empty string?, all lower case letters, hyphens and spaces are allowed but not at beginning or end of string
#assumptions/end goal - this function needs to return true if first and last letters of beast are same as dish. Return false if not.

#sample data
#("great blue heron", "garlic naan") = True
#("chick-a-dee", "chocolate cake") = True
#("chickadee", "chocolate croissant") = False
#("german*8shephard", "gluten snack") = False


#function feast takes two arguments, beast & dish
def feast(beast, dish):
#heck if the first letter and last letters are the same and return True if they are
   return beast[0] == dish[0] and beast[-1] == dish[-1]

