def compose(f,g):
    # Compose the two functions here!
    def newfunc(*args):
      return f(g(*args))
    return newfunc

