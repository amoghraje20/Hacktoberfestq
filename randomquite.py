import random

def random_quote():
    """Return a random motivational quote."""
    quotes = [
        "Code is poetry. 🐍",
        "Stay curious. Keep building. 💻",
        "Errors are just features in disguise. 😅",
        "Automate the boring stuff. 🚀",
        "You got this! 💪"
    ]
    return random.choice(quotes)

# Example
print(random_quote())  # e.g., "Automate the boring stuff. 🚀"
