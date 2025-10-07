from typing import Callable


def cache(func: Callable) -> Callable:
    func_cache = {}

    def wrapper(*args, **kwargs) -> Callable:
        cache_key = args
        if cache_key in func_cache:
            print("Getting from cache")
            return func_cache[cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            func_cache[cache_key] = result
            return result

    return wrapper
