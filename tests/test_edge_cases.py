"""Tests for edge cases and dunder methods."""

import pytest
from trie import Trie, TrieError


class TestDunderMethods:
    """Test special methods like __len__, __contains__, etc."""

    def test_len_empty_trie(self) -> None:
        """len() of empty trie is 0."""
        trie = Trie()
        assert len(trie) == 0

    def test_len_after_insert(self) -> None:
        """len() increases after insert."""
        trie = Trie()
        trie.insert("apple")
        assert len(trie) == 1

    def test_len_multiple_inserts(self) -> None:
        """len() counts unique words."""
        trie = Trie()
        trie.insert("apple")
        trie.insert("banana")
        trie.insert("cherry")
        assert len(trie) == 3

    def test_len_duplicate_insert(self) -> None:
        """len() unchanged by duplicate insert."""
        trie = Trie()
        trie.insert("apple")
        trie.insert("apple")
        assert len(trie) == 1

    def test_contains_word(self) -> None:
        """word in trie works (uses __contains__)."""
        trie = Trie()
        trie.insert("apple")
        assert "apple" in trie

    def test_contains_missing_word(self) -> None:
        """word not in trie works."""
        trie = Trie()
        trie.insert("apple")
        assert "banana" not in trie

    def test_contains_prefix(self) -> None:
        """prefix not in trie (only exact words)."""
        trie = Trie()
        trie.insert("apple")
        assert "app" not in trie

    def test_iter_empty_trie(self) -> None:
        """Iterating empty trie yields nothing."""
        trie = Trie()
        assert list(trie) == []

    def test_iter_single_word(self) -> None:
        """Iterating yields single word."""
        trie = Trie()
        trie.insert("apple")
        assert list(trie) == ["apple"]

    def test_iter_multiple_words(self) -> None:
        """Iterating yields words in sorted order."""
        trie = Trie()
        words = ["zebra", "apple", "monkey"]
        for word in words:
            trie.insert(word)
        assert list(trie) == ["apple", "monkey", "zebra"]

    def test_bool_empty_trie(self) -> None:
        """bool(empty_trie) is False."""
        trie = Trie()
        assert bool(trie) is False

    def test_bool_nonempty_trie(self) -> None:
        """bool(nonempty_trie) is True."""
        trie = Trie()
        trie.insert("apple")
        assert bool(trie) is True

    def test_repr(self) -> None:
        """repr() returns meaningful string."""
        trie = Trie()
        trie.insert("apple")
        repr_str = repr(trie)
        assert "Trie" in repr_str
        assert "1" in repr_str or "apple" in repr_str


class TestWords:
    """Test words() method."""

    def test_words_empty_trie(self) -> None:
        """words() on empty trie returns empty list."""
        trie = Trie()
        assert trie.words() == []

    def test_words_single_word(self) -> None:
        """words() returns single word."""
        trie = Trie()
        trie.insert("apple")
        assert trie.words() == ["apple"]

    def test_words_multiple_words(self) -> None:
        """words() returns all words."""
        trie = Trie()
        words = ["apple", "banana", "cherry"]
        for word in words:
            trie.insert(word)
        assert trie.words() == words

    def test_words_sorted_order(self) -> None:
        """words() returns words in sorted order."""
        trie = Trie()
        words = ["zebra", "apple", "monkey", "banana"]
        for word in words:
            trie.insert(word)
        assert trie.words() == ["apple", "banana", "monkey", "zebra"]

    def test_words_includes_empty_string(self) -> None:
        """words() includes empty string if inserted."""
        trie = Trie()
        trie.insert("")
        trie.insert("apple")
        words = trie.words()
        assert "" in words
        assert "apple" in words

    def test_words_after_delete(self) -> None:
        """words() reflects deletions."""
        trie = Trie()
        trie.insert("apple")
        trie.insert("banana")
        trie.delete("apple")
        assert trie.words() == ["banana"]


class TestEdgeCases:
    """Test various edge cases."""

    def test_words_with_whitespace(self) -> None:
        """Words with whitespace are supported."""
        trie = Trie()
        trie.insert("hello world")
        assert trie.search("hello world") is True

    def test_single_character_words(self) -> None:
        """Single character words work."""
        trie = Trie()
        for char in "abc":
            trie.insert(char)
        assert len(trie) == 3
        assert trie.search("a") is True

    def test_word_is_substring_of_another(self) -> None:
        """Word that is substring of another is tracked separately."""
        trie = Trie()
        trie.insert("testing")
        trie.insert("test")
        assert trie.search("test") is True
        assert trie.search("testing") is True

    def test_special_characters(self) -> None:
        """Words with special characters work."""
        trie = Trie()
        words = ["hello!", "test@123", "a-b-c", "x.y.z"]
        for word in words:
            trie.insert(word)
        for word in words:
            assert trie.search(word) is True

    def test_numeric_string_words(self) -> None:
        """Numeric strings as words work."""
        trie = Trie()
        trie.insert("123")
        trie.insert("456")
        assert trie.search("123") is True
        assert trie.autocomplete("1") == ["123"]

    def test_repeated_characters(self) -> None:
        """Words with repeated characters work."""
        trie = Trie()
        words = ["aaa", "aaaa", "aaaaa"]
        for word in words:
            trie.insert(word)
        for word in words:
            assert trie.search(word) is True

    def test_mixed_case_operations(self) -> None:
        """Mixed case is preserved and case-sensitive."""
        trie = Trie()
        trie.insert("HeLLo")
        assert trie.search("HeLLo") is True
        assert trie.search("hello") is False
        assert trie.search("HELLO") is False
