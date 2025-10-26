import time
from functools import wraps
from tabnanny import check

def run_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        r = func(*args, **kwargs)
        end_time = time.perf_counter()
        result = end_time - start_time
        print(f'The function {func.__name__}{args} run {result:.2f} seconds')
        return r
    return wrapper


def cache(func):
    d = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        k = args + tuple(sorted(kwargs.items()))
        if (k not in d):
            d[k] = func(*args, *kwargs)
        return d[k]
    return wrapper


def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@cache
def fibonacci_cached(n):
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = 30
print("Fibonacci without cache:")
run_time(fibonacci)(n)

print("\nFibonacci with cache:")
run_time(fibonacci_cached)(n)

print("\nFibonacci with cache again:")
run_time(fibonacci_cached)(n)