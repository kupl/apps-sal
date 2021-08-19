def solve(arr, n):
    dogs = [i for (i, x) in enumerate(arr) if x == 'D']
    cats = {i for (i, x) in enumerate(arr) if x == 'C'}
    catch = 0
    while dogs and cats:
        dog = dogs.pop()
        cat = max((cat for cat in cats if abs(dog - cat) <= n), default=-1)
        if cat >= 0:
            catch += 1
            cats.remove(cat)
    return catch
