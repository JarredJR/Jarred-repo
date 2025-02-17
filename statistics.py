def mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0


def median(numbers):
      sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]


def mode(numbers):
    from collections import Counter
    
    counts = Counter(numbers)
    max_count = max(counts.values())
    modes = [num for num, count in counts.items() if count == max_count]
    
    return modes[0] if len(modes) == 1 else modes 


if __name__ == "__main__":
    sample_data = [4, 1, 2, 2, 3, 4, 4, 5, 6]
    print("Mean:", mean(sample_data))
    print("Median:", median(sample_data))
    print("Mode:", mode(sample_data))
