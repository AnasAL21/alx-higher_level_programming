#!/usr/bin/python3
"""define an inherited list."""


class MyList(list):
    """Implements sorted printing for the built-in."""

    def print_sorted(self):
        """Print a list in sorted."""
        print(sorted(self))
