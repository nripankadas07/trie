"""TrieNode class for the prefix tree structure."""


class TrieNode:
    """A single node in the trie structure.

    Attributes:
        children: Dictionary mapping characters to child nodes.
        is_word: Boolean indicating if this node marks the end of a word.
    """

    def __init__(self) -> None:
        """Initialize an empty TrieNode."""
        self.children: dict[str, "TrieNode"] = {}
        self.is_word: bool = False
