archive = []
archive_values = {0: 0}
def count_squareable(n):
    def solve(nn):
        return next((1 for x in range(1, int(nn**.5)+1) if not nn%x and x%2==(nn//x)%2), 0)
    first_ind = next((i for i in reversed(archive) if i<=n), 0)
    result = sum(solve(i) for i in range(first_ind+1, n+1))+archive_values[first_ind]
    archive.append(n)
    archive_values[n] = result
    return result
