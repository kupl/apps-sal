def two_by_two(animals):
    return {animal: 2 for animal in set(animals) if animals.count(animal) > 1} if len(animals) else False
