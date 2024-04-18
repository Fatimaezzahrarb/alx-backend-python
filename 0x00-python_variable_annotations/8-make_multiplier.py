#!/usr/bin/env python3
"""functions"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
   
    def f(n: float) -> float:
        """ multiplies a float """
        return float(n * multiplier)

    return f
