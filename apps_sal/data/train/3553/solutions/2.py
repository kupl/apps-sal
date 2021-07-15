from re import match, compile
def show_me(name):
  return match(compile(r'^[A-Z][a-z]+(?:-[A-Z][a-z]+)*$'), name) != None
