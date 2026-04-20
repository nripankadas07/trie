"""Tests for delete operations."""

import pytest
from trie import Trie, TrieError


class TestDelete:
    """Test delete functionality."""

    def test_delete_nonexistent_word(self) -> None:
        """Delete nonexistent word returns False."""
        trie = Trie()
        result = trie.delete("apple")
        assert result is False

    def test_delete_existing_word(self) -> None:
        """Delete existing word returns True."""
        trie = Trie()
        trie.insert("apple")
        result = trie.delete("apple")
        assert result is True
        assert trie.search("apple") is False

    def test_delete_leaves_other_words(self) -> None:
        """Deleting word doesn't affect others."""
        trie = Trie()
        trie.insert("apple")
        trie.insert("application")
        trie.delete("apple")
        assert trie.search("application") is True

    def test_delete_word_that_is_prefix(self) -> None:
        """Delete word that is prefix of another word."""
        trie = Trie()
        trie.insert("app")
        trie.insert("apple")
        result = trie.delete("app")
        assert result is True
        assert trie.search("app") is False
        assert trie.search("apple") is True

    def test_delete_word_removes_unused_nodes(self) -> None:
        """Delete word removes unused nodes from trie."""
        trie = Trie()
        trie.insert("app")
        trie.delete("app")
        assert trie.starts_with("app") is False

    def test_delete_then_reinsert(self) -> None:
        """Delete and reinsert word works correctly."""
        trie = Trie()
        trie.insert("apple")
        trie.delete("apple")
        trie.insert("apple")
        assert trie.search("apple") is True

    def test_delete_empty_string(self) -> None:
        """Delete empty string."""
        trie = Trie()
        trie.insert("")
        assert trie.delete("") is True
        assert trie.search("") is False

    def test_delete_from_empty_trie(self) -> None:
        """Delete from empty trie returns False."""
        trie = Trie()
        assert trie.delete("apple") is False

    def test_delete_non_string_raises_error(self) -> None:
        """Delete with non-string raises TrieError."""
        trie = Trie()
        with pytest.raises(TrieError):
            trie.delete(123)  # type: ignore

    def test_delete_decrements_length(self) -> None:
        """Deleting word decrements trie length."""
        trie = Trie()
        trie.insert("apple")
        trie.insert("banana")
        assert len(trie) == 2
        trie.delete("apple")
        assert len(trie) == 1

    def test_delete_unicode_word(self) -> None:
        """Delete unicode word."""
        trie = Trie()
        trie.insert("café")
        assert trie.delete("café") is True
        assert trie.search("café") is False

    def test_delete_multiple_words_same_prefix(self) -> None:
        """Delete one word with shared prefix."""
        trie = Trie()
        trie.insert("car")
        trie.insert("card")
        trie.insert("care")
        trie.delete("card")
        assert trie.search("car") is True
        assert trie.search("card") is False
        assert trie.search("care") is True
