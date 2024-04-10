import json
from collections import Counter
from typing import List, Tuple


def load_data(filename: str) -> List[int]:
    """Load a list of integers from a JSON file."""
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            if isinstance(data, list) and all(isinstance(num, int) for num in data):
                return data
            else:
                raise ValueError("File does not contain a valid list of integers.")
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found.")
    except json.JSONDecodeError:
        raise ValueError(f"Unable to decode JSON file '{filename}'.")


def calculate_frequency(numbers: List[int]) -> List[Tuple[int, int]]:
    """Calculate the frequency of each unique number and return sorted by frequency descending."""
    counter = Counter(numbers)
    frequencies = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    return frequencies


def get_third_highest_frequency(frequencies: List[Tuple[int, int]]) -> Tuple[int, int]:
    """Retrieve the third highest frequency from the list of (number, frequency) tuples."""
    if len(frequencies) < 3:
        raise ValueError("The list doesn't contain at least three unique frequencies.")

    third_highest_freq = frequencies[2][1]
    for number, frequency in frequencies:
        if frequency == third_highest_freq:
            return number, frequency


def save_output(data: dict, filename: str) -> None:
    """Save the given data as JSON in a file."""
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError:
        print(f"Error: Unable to write data to file '{filename}'.")


def main():
    try:
        numbers = load_data('data.json')
        frequencies = calculate_frequency(numbers)
        third_highest_freq = get_third_highest_frequency(frequencies)

        output = {
            "sorted_frequency_distribution": frequencies,
            "third_highest_frequency": third_highest_freq
        }

        save_output(output, 'output.json')

        print("Output saved to output.json")
    except (ValueError, FileNotFoundError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
