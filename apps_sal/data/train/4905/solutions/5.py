def answer(puzzlebox):
    return 42


print(type(dir(puzzlebox)))
for i in dir(puzzlebox):
    print(i)
x = Puzzlebox()
print(x)
print(x.answer)
print(x.hint)
print(x.hint_two)
print(x.key)
print(x.lock(x.key))
