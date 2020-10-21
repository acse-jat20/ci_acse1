"""The functions to be tested according to lecture 7"""

from functools import lru_cache
__all__ = ['my_sum', 'factorial']


def my_sum(iterable):
    """Calculating a sum"""
    tot = 0
    for i in iterable:
        tot += i
    return tot

@lru_cache(maxsize=None)  # Note: -> @cache in python >= 3.9
def factorial(number):
    """Calculating a factorial"""
    return number * factorial(number-1) if n else 1
