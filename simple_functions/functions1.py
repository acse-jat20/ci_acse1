"""The functions to be tested according to lecture 7"""

from functools import lru_cache
from numpy import sqrt
__all__ = ['my_sum', 'factorial', 'solve_quadratic']


def my_sum(iterable):
    """Calculating a sum"""
    tot = 0
    for i in iterable:
        tot += i
    return tot


@lru_cache(maxsize=None)  # Note: -> @cache in python >= 3.9
def factorial(number):
    """Calculating a factorial"""
    return number * factorial(number-1) if number else 1


def solve_quadratic(a, b, c):
    """Solve a quadratic equation ax^2+bx+c=0 in the reals"""
    if b**2 - 4.0*a*c > 0:
        # two solutions
        return (
            (-b - sqrt(b**2 - 4.0*a*c))/(2.0*a),
            (-b + sqrt(b**2 - 4.0*a*c))/(2.0*a)
        )
    elif b**2 - 4.0*a*c == 0:
        # one solution
        return -b/(2.0*a)
    else:
        # no solutions
        return None
