COEFS = (('norm_kill', 100), ('assist', 50), ('damage', 0.5), ('healing', 1), ('env_kill', 500))


def scoring(arr):
    return [p['name'] for p in sorted(arr, key=lambda p: -(sum((p[k] * c for (k, c) in COEFS)) + 2 ** p['streak']))]
