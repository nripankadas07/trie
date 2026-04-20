"""Tests for autocomplete and prefix search operations."""

import pytest
from trie import Trie, TrieError


class TestAutocomplete:
    """Test autocomplete functionality."""

    def test_autocomplete_empty_trie(self) -> None:
        """Autocomplete on empty trie returns empty list."""
        trie = Trie()
        result = trie.autocomplete("a")
        assert result == []

    def test_autocomplete_single_match(self) -> None:
        """Autocomplete returns single matching word."""
        trie = Trie()
        trie.insert("apple")
        result = trie.autocomplete("app")
        assert result == ["apple"]

    def test_autocomplete_multiple_matches(self) -> None:
        """Autocomplete returns multiple matches in sorted order."""
        trie = Trie()
        words = ["apple", "app", "application"]
        for word in words:
            trie.insert(word)
        result = trie.autocomplete("app")
        assert result == ["app", "apple", "application"]

    def test_autocomplete_no_matches(self) -> None:
        """Autocomplete with no matches returns empty list."""
        trie = Trie()
        trie.insert("apple")
        result = trie.autocomplete("xyz")
        assert result == []

    def test_autocomplete_limit(self) -> None:
        """Autocomplete respects limit parameter."""
        trie = Trie()
        words = ["a", "ab", "abc", "abcd", "abcde"]
        for word in words:
            trie.insert(word)
        result = trie.autocomplete("a", limit=2)
        assert len(result) == 2
        assert result == ["a", "ab"]

    def test_autocomplete_limit_zero(self) -> None:
        """Autocomplete with limit=0 returns empty list."""
        trie = Trie()
        trie.insert("apple")
        result = trie.autocomplete("app", limit=0)
        assert result == []

    def test_autocomplete_limit_exceeds_matches(self) -> None:
        """Autocomplete limit exceeding matches returns all matches."""
        trie = Trie()
        trie.insert("apple")
        trie.insert("app")
        result = trie.autocomplete("app", limit=100)
        assert len(result) == 2

    def test_autocomplete_empty_prefix(self) -> None:
        """Autocomplete with empty prefix returns all words."""
        trie = Trie()
        words = ["apple", "banana", "cherry"]
        for word in words:
            trie.insert(word)
        result = trie.autocomplete("", limit=10)
        assert result == ["apple", "banana", "cherry"]

    def test_autocomplete_non_string_raises_error(self) -> None:
        """Autocomplete with non-string prefix raises TrieError."""
        trie = Trie()
        with pytest.raises(TrieError):
            trie.autocomplete(123)  # type: ignore

    def test_autocomplete_unicode_prefix(self) -> None:
        """Autocomplete works with unicode prefixes."""
        trie = Trie()
        trie.insert("café")
        trie.insert("cafeteria")
        result = trie.autocomplete("caf")
        assert len(result) == 2

    def test_autocomplete_sorted_order(self) -> None:
        """Autocomplete returns results in lexicographic order."""
        trie = Trie()
        words = ["zebra", "apple", "monkey", "banana"]
        for word in words:
            trie.insert(word)
        result = trie.autocomplete("", limit=10)
        assert result == ["apple", "banana", "monkey", "zebra"]


class TestStartsWith:
    """Test starts_with functionality."""

    def test_starts_with_empty_trie(self) -> None:
        """starts_with on empty trie returns False."""
        trie = Trie()
        assert trie.starts_with("a") is False

    def test_starts_with_exact_word(self) -> None:
        """starts_with returns True for exact word."""
        trie = Trie()
        trie.insert("apple")
        assert trie.starts_with("apple") is True

    def test_starts_with_prefix(self) -> None:
        """starts_with returns True for valid prefix."""
        trie = Trie()
        trie.insert("apple")
        assert trie.starts_with("app") is True

    def test_starts_with_no_match(self) -> None:
        """starts_with returns False for non-existent prefix."""
        trie = Trie()
        trie.insert("apple")
        assert trie.starts_with("xyz") is False

    def test_starts_with_empty_prefix(self) -> None:
        """starts_with empty prefix returns True if trie non-empty."""
        trie = Trie()
        trie.insert("apple")
        assert trie.starts_with("") is True

    def test_starts_with_empty_prefix_empty_trie(self) -> None:
        """starts_with empty prefix on empty trie returns False."""
        trie = Trie()
        assert trie.starts_with("") is False

    def test_starts_with_non_string_raises_error(self) -> None:
        """starts_with with non-string raises TrieError."""
        trie = Trie()
        with pytest.raises(TrieError):
            trie.starts_with(123)  # type: ignore

    def test_starts_with_unicode(self) -> None:
        """starts_with works with unicode."""
        trie = Trie()
        trie.insert("café")
        assert trie.starts_with("caf") is True
        assert trie.starts_with("café") is True


class TestCountPrefix:
    """Test count_prefix functionality."""

    def test_count_prefix_empty_trie(self) -> None:
        """count_prefix on empty trie returns 0."""
        trie = Trie()
        assert trie.count_prefix("a") == 0

    def test_count_prefix_single_word(self) -> None:
        """count_prefix for single matching word returns 1."""
        trie = Trie()
        trie.insert("apple")
        assert trie.count_prefix("app") == 1

    def test_count_prefix_multiple_words(self) -> None:
        """count_prefix counts all words with prefix."""
        trie = Trie()
        words = ["apple", "app", "application"]
        for word in words:
            trie.insert(word)
        assert trie.count_prefix("app") == 3

    def test_count_prefix_no_matches(self) -> None:
        """count_prefix with no matches returns 0."""
        trie = Trie()
        trie.insert("apple")
        assert trie.count_prefix("xyz") == 0

    def test_count_prefix_empty_prefix(self) -> None:
        """count_prefix with empty prefix returns total words."""
        trie = Trie()
        words = ["apple", "banana", "cherry"]
        for word in words:
            trie.insert(word)
        assert trie.count_prefix("") == 3

    def test_count_prefix_non_string_raises_error(self) -> None:
        """count_prefix with non-string raises TrieError."""
        trie = Trie()
        with pytest.raises(TrieError):
            trie.count_prefix(123)  # type: ignore
