
def answer(puzzlebox):
    return(42)


print((dir(puzzlebox)))
print((list(dir(puzzlebox))[25:30]))

print((puzzlebox.answer))
print((puzzlebox.hint))
print((puzzlebox.hint_two))
print((puzzlebox.key))
print((puzzlebox.lock))

num = 2
float = 2.3
bool = False
str = "hello"

print((puzzlebox.lock(num)))
print((puzzlebox.lock(float)))
print((puzzlebox.lock(bool)))
print((puzzlebox.lock(str)))
print((puzzlebox.lock(puzzlebox.key)))
