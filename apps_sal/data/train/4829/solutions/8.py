def compose(f,g):
  def inner(*args, **kwargs):
    return f(g(*args, **kwargs))
  return inner
