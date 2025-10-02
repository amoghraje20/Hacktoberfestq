def most_frequent(lst):
    """Return the most common item in a list."""
    if not lst:
        return None
    return max(set(lst), key=lst.count)

# Example
colors = ['red', 'blue', 'red', 'green', 'red']
print(most_frequent(colors))  # "red"
