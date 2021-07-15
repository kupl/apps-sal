import re
def rake_garden(g):
  return re.sub(r'\b(?!gravel|rock\b)\w+','gravel',g)
