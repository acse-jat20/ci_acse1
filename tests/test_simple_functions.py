"""Testing simple functions according to lecture 7."""

import pytest

from simple_functions import my_sum
from simple_functions import factorial
from simple_functions import solve_quadratic


class TestSimpleFunctions(object):
    '''Class to test our simple functions are working correctly'''

    @pytest.mark.parametrize('iterable, expected', [
        ([8, 7, 5], 20),
        ((10, -2, 5, -10, 1), 4)
    ])
    def test_my_add(self, iterable, expected):
        '''Test our add function'''
        isum = my_sum(iterable)
        assert isum == expected

    @pytest.mark.parametrize('number, expected', [
        (5, 120),
        (3, 6),
        (1, 1)
    ])
    def test_factorial(self, number, expected):
        '''Test our factorial function'''
        answer = factorial(number)
        assert answer == expected

    @pytest.mark.parametrize('a, b, c, expected', [
        (1, 0, -1, (-1.0, 1.0)),
        (1, 0, 0, (0.0)),
        (1, 0, 1, None)
    ])
    def test_quadratic(self, a, b, c, expected):
        '''Test our factorial function'''
        answer = solve_quadratic(a, b, c)
        assert answer == expected
