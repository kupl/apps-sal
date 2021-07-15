def remove_smallest(numbers):
    try:
        ind = numbers.index(min(numbers))
        return numbers[:ind]+numbers[ind+1:]
    except ValueError:
        return []
    except:
        return []
