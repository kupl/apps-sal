def friend_find(line):
    possible_combo = (['blue', 'blue', 'red'], ['blue', 'red', 'blue'], ['red', 'blue', 'blue'])
    return len({i + line[i:i + 3].index('red') for i in range(len(line)) if line[i:i + 3] in possible_combo})
