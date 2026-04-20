# Trie

A production-quality prefix tree (trie) data structure implementation in Python with fast prefix search, autocomplete, and pattern matching.

## Installation

```bash
pip install trie
```

Or install from source:

```bash
git clone https://github.com/nripankadas07/trie.git
cd trie
pip install -e .
```

## Quick Start

```python
from trie import Trie

# Create a trie
trie = Trie()

# Insert words
trie.insert("apple")
trie.insert("app")
trie.insert("application")
trie.insert("apply")

# Search for exact words
trie.search("apple")        # True
trie.search("app")          # True
trie.search("appl")         # False (prefix, not a word)

# Check if prefix exists
trie.starts_with("app")     # True
trie.starts_with("xyz")     # False

# Autocomplete
trie.autocomplete("app", limit=10)  # ["app", "apple", "application", "apply"]

# Count words with prefix
trie.count_prefix("app")    # 4

# Delete a word
trie.delete("app")          # True
trie.search("app")          # False

# Get all words
trie.words()                # ["apple", "application", "apply"]

# Use dictionary-like operations
"apple" in trie             # True
len(trie)                   # 3
bool(trie)                  # True
for word in trie:
    print(word)             # Iterates in sorted order
```

## API Reference

### Trie

Main class for the prefix tree data structure.

#### Constructor

```python
Trie() -> Trie
```

Creates an empty trie.

#### Methods

##### `insert(word: str) -> None`

Insert a word into the trie. If the word already exists, this is a no-op.

**Args:**
- `word`: The word to insert (must be a string)

**Raises:**
- `TrieError`: If `word` is not a string

**Example:**
```python
trie.insert("hello")
```

##### `search(word: str) -> bool`

Check if an exact word exists in the trie.

**Args:**
- `word`: The word to search for (must be a string)

**Returns:**
- `True` if the word exists, `False` otherwise

**Raises:**
- `TrieError`: If `word` is not a string

**Example:**
```python
if trie.search("hello"):
    print("Word found!")
```

##### `delete(word: str) -> bool`

Delete a word from the trie.

**Args:**
- `word`: The word to delete (must be a string)

**Returns:**
- `True` if the word was deleted, `False` if it didn't exist

**Raises:**
- `TrieError`: If `word` is not a string

**Example:**
```python
if trie.delete("hello"):
    print("Word deleted!")
```

##### `starts_with(prefix: str) -> bool`

Check if any word in the trie starts with the given prefix.

**Args:**
- `prefix`: The prefix to check (must be a string)

**Returns:**
- `True` if at least one word starts with the prefix, `False` otherwise

**Raises:**
- `TrieError`: If `prefix` is not a string

**Example:**
```python
if trie.starts_with("hel"):
    print("Words with prefix 'hel' exist!")
```

##### `autocomplete(prefix: str, limit: int = 10) -> list[str]`

Return words that start with the given prefix, up to a limit.

**Args:**
- `prefix`: The prefix to search for (must be a string)
- `limit`: Maximum number of results to return (default: 10)

**Returns:**
- List of matching words in sorted order (empty list if no matches)

**Raises:**
- `TrieError`: If `prefix` is not a string or `limit` is negative

**Example:**
```python
suggestions = trie.autocomplete("hel", limit=5)
# Returns up to 5 words starting with "hel"
```

##### `count_prefix(prefix: str) -> int`

Count how many words start with the given prefix.

**Args:**
- `prefix`: The prefix to count (must be a string)

**Returns:**
- Number of words with the given prefix

**Raises:**
- `TrieError`: If `prefix` is not a string

**Example:**
```python
count = trie.count_prefix("app")
```

##### `words() -> list[str]`

Return all words in the trie in sorted order.

**Returns:**
- List of all words, sorted lexicographically

**Example:**
```python
all_words = trie.words()
```

#### Special Methods

##### `__len__() -> int`

Return the number of words in the trie.

```python
num_words = len(trie)
```

##### `__contains__(word: str) -> bool`

Check if a word is in the trie using the `in` operator.

```python
if "hello" in trie:
    print("Found!")
```

##### `__iter__()`

Iterate over all words in the trie in sorted order.

```python
for word in trie:
    print(word)
```

##### `__bool__() -> bool`

Return `True` if the trie is non-empty, `False` otherwise.

```python
if trie:
    print("Trie has words")
```

##### `__repr__() -> str`

Return a string representation of the trie.

```python
print(repr(trie))  # Trie(5 words)
```

### Exceptions

#### `TrieError`

Exception raised for invalid operations on the Trie.

```python
from trie import TrieError

try:
    trie.insert(123)  # Invalid: not a string
except TrieError as e:
    print(f"Error: {e}")
```

## Running Tests

### Prerequisites

Install the package with dev dependencies:

```bash
pip install -e ".[dev]"
```

### Run Tests

From the project root:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=src/trie
```

Run specific test file:

```bash
pytest tests/test_insert_search.py -v
```

Run with verbose output:

```bash
pytest -v
```

## Design Highlights

- **Efficient**: O(m) time complexity for insert, search, and delete operations, where m is the length of the word
- **Memory-efficient**: Shares common prefixes across words
- **Type-safe**: Full type hints for all public APIs
- **Well-tested**: 60+ tests covering happy paths and edge cases
- **Production-ready**: Error handling, Unicode support, comprehensive documentation
- **Pythonic**: Supports standard operations like `in`, `len()`, iteration, and boolean evaluation

## Edge Cases Handled

- Empty string insertion and search
- Non-string input validation (raises `TrieError`)
- Deleting non-existent words
- Deleting words that are prefixes of other words
- Autocomplete with no matches (returns empty list)
- Very long words (1000+ characters)
- Unicode characters and strings
- Empty trie operations
- Duplicate inserts (idempotent)

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please ensure:

1. All tests pass: `pytest`
2. Code is formatted: `black src tests`
3. No linting errors: `ruff check src tests`
4. Type checking passes: `mypy src`

## Author

nripankadas07

## Changelog

### Version 1.0.0

- Initial production release
- Full Trie implementation with 8 core methods
- Support for prefix search, autocomplete, and word counting
- Comprehensive test suite (60+ tests)
- Type hints and documentation
