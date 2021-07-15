import re
def compare(a, b):

  def scoreCSS(s):
    d = {'#':0, '.':0, ' ':0}
    for c in re.findall("[#\. ](?=[\w-])", " {}".format(s)):
        d[c] = d[c] + 1
    return (d['#'], d['.'], d[' '])
  
  return a if (scoreCSS(a) > scoreCSS(b)) else b

