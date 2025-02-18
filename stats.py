from collections import Counter

def mean(numbers):
    """Calculate and return the mean (average) of a list of numbers."""
    return sum(numbers) / len(numbers) if numbers else None

def median(numbers):
    """Calculate and return the median of a list of numbers."""
    if not numbers:
        return None

    numbers.sort()
    n = len(numbers)
    mid = n // 2

    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2  # Average of middle two
    else:
        return numbers[mid]  # Middle number

def mode(numbers):
    """Calculate and return the mode of a list of numbers."""
    if not numbers:
        return None

    counts = Counter(numbers)
    max_count = max(counts.values())
    modes = [num for num, count in counts.items() if count == max_count]

    return modes[0] if len(modes) == 1 else modes  # Return a single mode or a list of modes

def get_user_numbers():
    """Prompt the user to enter a list of numbers and return them as a list."""
    while True:
        try:
            user_input = input("Enter numbers separated by spaces: ")
            numbers = [float(num) for num in user_input.split()]
            if numbers:
                return numbers
        except ValueError:
            print("Invalid input. Please enter only numbers separated by spaces.")

if __name__ == "__main__":
    numbers = get_user_numbers()  # Get numbers from user

    print("\nNumbers:", numbers)
    print("Mean:", mean(numbers))
    print("Median:", median(numbers))
    print("Mode:", mode(numbers))

    input("\nPress Enter to exit...")  # Keeps terminal open

