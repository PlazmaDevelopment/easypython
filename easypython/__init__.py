"""
EasyPython - A module that makes Python even easier to use.

This module provides simplified interfaces and utility functions to make
Python development more intuitive and less verbose while maintaining
full functionality.
"""

from .core import (
    # Collections
    List, Dict, Set, Tuple, 
    # Types
    Int, Float, Str, Bool, Any, Optional, Union, 
    # Utilities
    print_all, count_chars, to_json, from_json,
    # File Operations
    read_file, write_file, append_file,
    # Functional Programming
    map_list, filter_list, reduce_list,
    # String Operations
    to_upper, to_lower, strip_whitespace,
    # Math
    add, subtract, multiply, divide, power
)

__version__ = '0.1.0'
