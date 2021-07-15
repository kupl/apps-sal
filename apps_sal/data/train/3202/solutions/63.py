def greet(name, owner):
  greetings = ["Hello boss", "Hello guest"]

  return greetings[0] if name == owner else greetings[1]

