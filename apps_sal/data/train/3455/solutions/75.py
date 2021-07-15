disarium_number = lambda n: 'Disarium !!' if n == sum(int(d) ** (i + 1) for i, d in enumerate(str(n))) else 'Not !!'
