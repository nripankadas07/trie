"""Tests for insert and search operations."""

import pytest
from trie import Trie, TrieError


class TestInsertAndSearch:
    """Test basic insert and search functionality."""

    def test_search_empty_trie(self) -> None:
        """Searching in empty trie returns False."""
        trie = Trie()
        assert trie.search("hello") is False

    def test_insert_and_search_single_word(self) -> None:
        """Insert and search a single word."""
        trie = Trie()
        trie.insert("hello")
        assert trie.search("hello") is True

    def test_search_nonexistent_word(self) -> None:
        """Search for word not in trie returns False."""
        trie = Trie()
        trie.insert("hello")
        assert trie.search("world") is False

    def test_insert_multiple_words(self) -> None:
        """Insert multiple words and search for each."""
        trie = Trie()
        words = ["apple", "app", "application", "banana", "band"]
        for word in words:
            trie.insert(word)
        for word in words:
            assert trie.search(word) is True

    def test_insert_duplicate_word(self) -> None:
        """Inserting duplicate word is idempotent."""
        trie = Trie()
        trie.insert("hello")
        trie.insert("hello")
        assert trie.search("hello") is True
        assert len(trie) == 1

    def test_search_prefix_is_not_word(self) -> None:
        """Searching for prefix returns False if not inserted as word."""
        trie = Trie()
        trie.insert("apple")
        assert trie.search("app") is False

    def test_insert_empty_string(self) -> None:
        """Inserting empty string should work."""
        trie = Trie()
        trie.insert("")
        assert trie.search("") is True

    def test_search_empty_string_in_empty_trie(self) -> None:
        """Searching for empty string in empty trie returns False."""
        trie = Trie()
        assert trie.search("") is False

    def test_insert_non_string_raises_error(self) -> None:
        """Inserting non-string raises TrieError."""
        trie = Trie()
        with pytest.raises(TrieError):
            trie.insert(123)  # type: ignore

    def test_insert_unicode_words(self) -> None:
        """Insert and search unicode words."""
        trie = Trie()
        words = ["café", "naïve", "日本", "🎉"]
        for word in words:
            trie.insert(word)
        for word in words:
            assert trie.search(word) is True

    def test_insert_very_long_word(self) -> None:
        """Insert and search very long word (1000+ chars)."""
        trie = Trie()
        long_word = "a" * 1000
        trie.insert(long_word)
        assert trie.search(long_word) is True

    def test_insert_case_sensitive(self) -> None:
        """Insert and search are case-sensitive."""
        trie = Trie()
        trie.insert("Hello")
        assert trie.search("hello") is False
        assert trie.search("Hello") is True

    def test_search_non_string_raises_error(self) -> None:
        """Searching for non-string raises TrieError."""
        trie = Trie()
        with pytest.raises(TrieError):
            trie.search(123)  # type: ignore
