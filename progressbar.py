import time

def progress_bar(total, delay=0.1):
    """Display a simple progress bar in the terminal."""
    for i in range(total + 1):
        percent = i * 100 // total
        bar = "█" * (i * 20 // total) + "-" * (20 - i * 20 // total)
        print(f"\rProgress: |{bar}| {percent}%", end="", flush=True)
        time.sleep(delay)
    print("\n✅ Done!")

# Example (10-step progress)
progress_bar(10)
