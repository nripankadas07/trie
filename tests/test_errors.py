"""Tests for error handling."""

import pytest
from trie import Trie, TrieError


class TestErrorHandling:
    """Test error handling across operations."""

    def test_trie_error_is_exception(self) -> None:
        """TrieError is an Exception subclass."""
        assert issubclass(TrieError, Exception)

    def test_insert_none_raises_error(self) -> None:
        """Inserting None raises TrieError."""
        trie = Trie()
        with pytest.raises(TrieError):
            trie.insert(None)  # type: ignore

    def test_insert_list_raises_error(self) -> None:
        """Inserting list raises TrieError."""
        trie = Trie()
        with pytest.raises(TrieError):
            trie.insert(["apple"])  # type: ignore

    def test_insert_dict_raises_error(self) -> None:
        """Inserting dict raises TrieError."""
        trie = Trie()
        with pytest.raises(TrieError):
            trie.insert({"word": "apple"})  # type: ignore

    def test_search_none_raises_error(self) -> None:
        """Searching for None raises TrieError."""
        trie = Trie()
        with pytest.raises(TrieError):
            trie.search(None)  # type: ignore

    def test_delete_none_raises_error(self) -> None:
        """Deleting None raises TrieError."""
        trie = Trie()
        with pytest.raises(TrieError):
            trie.delete(None)  # type: ignore

    def test_starts_with_none_raises_error(self) -> None:
        """starts_with None raises TrieError."""
        trie = Trie()
        with pytest.raises(TrieError):
            trie.starts_with(None)  # type: ignore

    def test_autocomplete_negative_limit_raises_error(self) -> None:
        """Autocomplete with negative limit raises TrieError."""
        trie = Trie()
        with pytest.raises(TrieError):
            trie.autocomplete("a", limit=-1)

    def test_count_prefix_none_raises_error(self) -> None:
        """count_prefix with None raises TrieError."""
        trie = Trie()
        with pytest.raises(TrieError):
            trie.count_prefix(None)  # type: ignore
