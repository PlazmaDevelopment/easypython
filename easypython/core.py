"""
Core functionality for EasyPython module.

This module provides simplified interfaces and utility functions to make
Python development more intuitive and less verbose.
"""

import json
import math
import os
from typing import Any, Callable, Iterable, List, Dict, Set, Tuple, TypeVar, Union, Optional

# Type aliases for better readability
T = TypeVar('T')
R = TypeVar('R')

# Collection types for easier imports
List = list
Dict = dict
Set = set
Tuple = tuple

# Type hints for cleaner code
Int = int
Float = float
Str = str
Bool = bool
Any = Any
Optional = Optional
Union = Union

# Constants
EMPTY = ""
SPACE = " "
NEWLINE = "\n"
TAB = "\t"

# String Operations
def to_upper(s: str) -> str:
    """Convert string to uppercase."""
    return s.upper()

def to_lower(s: str) -> str:
    """Convert string to lowercase."""
    return s.lower()

def strip_whitespace(s: str) -> str:
    """Remove leading and trailing whitespace from a string."""
    return s.strip()

def count_chars(s: str, char: str) -> int:
    """Count occurrences of a character in a string."""
    return s.count(char)

# File Operations
def read_file(file_path: str) -> str:
    """Read the entire content of a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(file_path: str, content: str, mode: str = 'w') -> None:
    """Write content to a file."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, mode, encoding='utf-8') as f:
        f.write(content)

def append_file(file_path: str, content: str) -> None:
    """Append content to a file."""
    write_file(file_path, content, 'a')

# JSON Operations
def to_json(data: Any, indent: int = 4, ensure_ascii: bool = False) -> str:
    """Convert Python object to JSON string."""
    return json.dumps(data, indent=indent, ensure_ascii=ensure_ascii)

def from_json(json_str: str) -> Any:
    """Convert JSON string to Python object."""
    return json.loads(json_str)

# Functional Programming
def map_list(func: Callable[[T], R], iterable: Iterable[T]) -> List[R]:
    """Apply a function to every item of an iterable and return a list of results."""
    return [func(item) for item in iterable]

def filter_list(func: Callable[[T], bool], iterable: Iterable[T]) -> List[T]:
    """Construct a list from those elements of iterable for which function returns true."""
    return [item for item in iterable if func(item)]

def reduce_list(func: Callable[[T, T], T], iterable: Iterable[T], initial: T = None) -> T:
    """Apply a function of two arguments cumulatively to the items of an iterable."""
    it = iter(iterable)
    if initial is None:
        try:
            value = next(it)
        except StopIteration:
            raise TypeError("reduce() of empty sequence with no initial value") from None
    else:
        value = initial
    
    for element in it:
        value = func(value, element)
    return value

# Math Operations
def add(*args: Union[int, float]) -> Union[int, float]:
    """Add all the arguments together."""
    return sum(args)

def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Subtract b from a."""
    return a - b

def multiply(*args: Union[int, float]) -> Union[int, float]:
    """Multiply all the arguments together."""
    result = 1
    for num in args:
        result *= num
    return result

def divide(a: Union[int, float], b: Union[int, float]) -> float:
    """Divide a by b."""
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

def power(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
    """Raise base to the power of exponent."""
    return math.pow(base, exponent)

# Utility Functions
def print_all(*args, sep: str = ' ', end: str = '\n', file=None, flush: bool = False) -> None:
    """Print all arguments, converting them to strings if necessary."""
    print(*args, sep=sep, end=end, file=file, flush=flush)
