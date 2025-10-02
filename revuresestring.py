def reverse_string(s):
    """Reverse a string using a loop (educational)."""
    result = ""
    for char in s:
        result = char + result
    return result

# Example
print(reverse_string("hello"))  # "olleh"
