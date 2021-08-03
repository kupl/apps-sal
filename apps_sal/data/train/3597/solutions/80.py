from typing import List


def say_hello(name: List[str], city: str, state: str) -> str:
    return f"Hello, {' '.join(name)}! Welcome to {city}, {state}!"
