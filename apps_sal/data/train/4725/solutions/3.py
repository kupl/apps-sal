def reverse(n):
    """Returns n with all digits reversed. Assume positive n."""
    rev = lambda n, r: rev(n // 10, 10 * r + n % 10) if n > 0 else r
    return rev(n, 0)
