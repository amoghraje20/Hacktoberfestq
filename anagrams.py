def is_anagram(str1, str2):
    """Check if two strings are anagrams (ignores case & spaces)."""
    def clean(s):
        return sorted(c.lower() for c in s if c.isalnum())
    return clean(str1) == clean(str2)

# Example
print(is_anagram("listen", "silent"))      # True
print(is_anagram("hello", "bello"))        # False
