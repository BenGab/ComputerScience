def fib1(n: int) -> int:
    if n < 2:
        return n

    return fib1(n-1) + fib1(n-2)

from typing import Dict, Generator

memo: Dict[int, int] = {0: 0, 1: 1}

def fib2(n: int) -> int:
    if n in memo:
        return memo[n]
    
    memo[n] = fib2(n-1) + fib2(n-2)
    return memo[n]

def fib3(n: int) -> int:
    if n == 0: return n
    last: int = 0
    next: int = 1

    for _ in range(1, n):
        last, next = next, next + last
    return next

def fib4(n: int) -> Generator[int, None, None] :
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, next + last
        yield next

if __name__ == "__main__":
    print(fib1(5))
    print(fib1(10))
    print(fib2(50))
    print(fib3(50))
    for i in fib4(50):
        print(i)