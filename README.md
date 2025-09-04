# EasyPython

A Python module designed to make Python even easier to use by providing simplified interfaces and utility functions while maintaining full functionality.

## Features

- **Simplified Type Hints**: Cleaner syntax for type hints
- **String Operations**: Common string manipulations made easier
- **File Operations**: Simplified file handling
- **JSON Handling**: Easy JSON serialization/deserialization
- **Functional Programming**: Map, filter, and reduce with cleaner syntax
- **Math Operations**: Common mathematical operations

## Installation

```bash
pip install easypython
```

## Usage

### Basic Usage

```python
from easypython import *

# String operations
text = "  Hello, World!  "
print(strip_whitespace(text))  # "Hello, World!"
print(to_upper(text))         # "  HELLO, WORLD!  "

# Math operations
print(add(1, 2, 3, 4))       # 10
print(multiply(2, 3, 4))     # 24

# Functional programming
numbers = [1, 2, 3, 4, 5]
squared = map_list(lambda x: x**2, numbers)  # [1, 4, 9, 16, 25]
evens = filter_list(lambda x: x % 2 == 0, numbers)  # [2, 4]

# File operations
write_file("test.txt", "Hello, World!")
content = read_file("test.txt")  # "Hello, World!"

# JSON operations
data = {"name": "John", "age": 30}
json_str = to_json(data)  # '{\n    "name": "John",\n    "age": 30\n}'
parsed = from_json(json_str)  # {'name': 'John', 'age': 30}
```

### Type Hints

```python
from easypython import List, Dict, Set, Tuple, Int, Float, Str, Bool

def process_data(names: List[Str], config: Dict[Str, Any]) -> Tuple[Bool, Str]:
    # Function implementation
    pass
```

## API Reference

### String Operations
- `to_upper(s: str) -> str`: Convert string to uppercase
- `to_lower(s: str) -> str`: Convert string to lowercase
- `strip_whitespace(s: str) -> str`: Strip whitespace from string
- `count_chars(s: str, char: str) -> int`: Count character occurrences

### File Operations
- `read_file(file_path: str) -> str`: Read file content
- `write_file(file_path: str, content: str, mode: str = 'w') -> None`: Write to file
- `append_file(file_path: str, content: str) -> None`: Append to file

### JSON Operations
- `to_json(data: Any, indent: int = 4, ensure_ascii: bool = False) -> str`: Convert to JSON
- `from_json(json_str: str) -> Any`: Parse JSON string

### Functional Programming
- `map_list(func: Callable, iterable: Iterable) -> List`: Map function to iterable
- `filter_list(func: Callable, iterable: Iterable) -> List`: Filter iterable
- `reduce_list(func: Callable, iterable: Iterable, initial: Any = None) -> Any`: Reduce iterable

### Math Operations
- `add(*args) -> Number`: Sum all arguments
- `subtract(a, b) -> Number`: Subtract b from a
- `multiply(*args) -> Number`: Multiply all arguments
- `divide(a, b) -> float`: Divide a by b
- `power(base, exponent) -> Number`: Raise base to power of exponent

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT
