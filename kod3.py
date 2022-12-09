from typing import Callable

add_one: Callable[[int], int] = lambda x: x + 1
print(add_one(4))
foo: Callable[[int, str], str] = lambda a, b: f"{a}{b}"
print(foo(4, "assdsad"))
foo2 = lambda a, b: f"{a}{b}"
