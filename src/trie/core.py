"""Core Trie data structure implementation."""

from trie.errors import TrieError
from trie.node import TrieNode


class Trie:
    """A prefix tree (trie) data structure for efficient prefix search and autocomplete.

    The Trie supports fast word insertion, search, and prefix-based operations
    in O(m) time where m is the length of the word/prefix.
    """

    def __init__(self) -> None:
        """Initialize an empty Trie."""
        self._root = TrieNode()
        self._word_count = 0

    def insert(self, word: str) -> None:
        """Insert a word into the trie.

        Args:
            word: The word to insert.

        Raises:
            TrieError: If word is not a string.
        """
        if not isinstance(word, str):
            raise TrieError(f"Expected str, got {type(word).__name__}")

        node = self._root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        if not node.is_word:
            node.is_word = True
            self._word_count += 1

    def search(self, word: str) -> bool:
        """Check if an exact word exists in the trie.

        Args:
            word: The word to search for.

        Returns:
            True if the word exists, False otherwise.

        Raises:
            TrieError: If word is not a string.
        """
        if not isinstance(word, str):
            raise TrieError(f"Expected str, got {type(word).__name__}")

        node = self._root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def delete(self, word: str) -> bool:
        """Delete a word from the trie.

        Args:
            word: The word to delete.

        Returns:
            True if the word was deleted, False if it didn't exist.

        Raises:
            TrieError: If word is not a string.
        """
        if not isinstance(word, str):
            raise TrieError(f"Expected str, got {type(word).__name__}")

        def _delete_helper(node: TrieNode, word: str, index: int) -> bool:
            if index == len(word):
                if not node.is_word:
                    return False
                node.is_word = False
                return len(node.children) == 0

            char = word[index]
            if char not in node.children:
                return False

            child = node.children[char]
            should_delete_child = _delete_helper(child, word, index + 1)

            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0 and not node.is_word
            return False

        if not self.search(word):
            return False

        _delete_helper(self._root, word, 0)
        self._word_count -= 1
        return True

    def starts_with(self, prefix: str) -> bool:
        """Check if any word in the trie starts with the given prefix.

        Args:
            prefix: The prefix to check.

        Returns:
            True if at least one word starts with prefix, False otherwise.

        Raises:
            TrieError: If prefix is not a string.
        """
        if not isinstance(prefix, str):
            raise TrieError(f"Expected str, got {type(prefix).__name__}")

        if not self._word_count:
            return False

        node = self._root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def autocomplete(self, prefix: str, limit: int = 10) -> list[str]:
        """Return words that start with the given prefix, up to limit.

        Args:
            prefix: The prefix to search for.
            limit: Maximum number of results to return (default 10).

        Returns:
            List of matching words in sorted order.

        Raises:
            TrieError: If prefix is not a string or limit is negative.
        """
        if not isinstance(prefix, str):
            raise TrieError(f"Expected str, got {type(prefix).__name__}")
        if not isinstance(limit, int) or limit < 0:
            raise TrieError(f"Limit must be non-negative integer, got {limit}")

        if limit == 0:
            return []

        node = self._root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        results: list[str] = []
        self._dfs_collect(node, prefix, results, limit)
        return sorted(results)

    def count_prefix(self, prefix: str) -> int:
        """Count how many words start with the given prefix.

        Args:
            prefix: The prefix to count.

        Returns:
            Number of words with the given prefix.

        Raises:
            TrieError: If prefix is not a string.
        """
        if not isinstance(prefix, str):
            raise TrieError(f"Expected str, got {type(prefix).__name__}")

        node = self._root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]

        return self._count_words(node)

    def words(self) -> list[str]:
        """Return all words in the trie in sorted order.

        Returns:
            List of all words, sorted lexicographically.
        """
        results: list[str] = []
        self._dfs_collect(self._root, "", results, float("inf"))
        return sorted(results)

    def __len__(self) -> int:
        """Return the number of words in the trie."""
        return self._word_count

    def __contains__(self, word: object) -> bool:
        """Check if a word is in the trie using 'in' operator."""
        if not isinstance(word, str):
            return False
        return self.search(word)

    def __iter__(self):
        """Iterate over all words in the trie in sorted order."""
        return iter(self.words())

    def __bool__(self) -> bool:
        """Return True if trie is non-empty."""
        return self._word_count > 0

    def __repr__(self) -> str:
        """Return string representation of the trie."""
        return f"Trie({self._word_count} word{'s' if self._word_count != 1 else ''})"

    def _dfs_collect(
        self,
        node: TrieNode,
        prefix: str,
        results: list[str],
        limit: int | float,
    ) -> None:
        """Recursively collect words from a node via DFS.

        Args:
            node: Current node in traversal.
            prefix: Current prefix built so far.
            results: List to accumulate results.
            limit: Maximum results to collect.
        """
        if len(results) >= limit:
            return

        if node.is_word:
            results.append(prefix)

        for char, child in sorted(node.children.items()):
            self._dfs_collect(child, prefix + char, results, limit)

    def _count_words(self, node: TrieNode) -> int:
        """Count all words under a given node.

        Args:
            node: Node to count from.

        Returns:
            Number of complete words under this node.
        """
        count = 1 if node.is_word else 0
        for child in node.children.values():
            count += self._count_words(child)
        return count
