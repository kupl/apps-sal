def greet(x): return "Hello " + x[0].upper() + x[1:-1].lower() + x[-1].lower() + "!" if len(x) != 1 else "Hello " + x[0].upper() + "!"
