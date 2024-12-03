"""Advent of Code solution for day 3: Mull It Over"""

import re

def load_input(file_path):
    """
    Load content of file into a string

    :param file_path: File path
    :type file_path: str
    :return: File content
    :rtype: str
    """

    with open(file_path, encoding='utf-8') as f:
        corrupted_memory = f.read()

    return corrupted_memory

def part_1(corrupted_memory):
    """
    This function extracts pairs of numbers from a string that follows the pattern "mul(X,Y)",
    where X and Y are 1 to 3 digit numbers. For each pair, it multiplies the numbers and then
    sums up the results of all multiplications.

    :param corrupted_memory: File content
    :type corrupted_memory: str
    :return: Sum of multiplications
    :rtype: int
    """

    sum_of_products = 0
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, corrupted_memory)
    for num1, num2 in matches:
        sum_of_products += int(num1) * int(num2)

    return sum_of_products

def part_2(corrupted_memory):
    """
    This function extracts pairs of numbers from a string that follows the pattern "mul(X,Y)",
    where X and Y are 1 to 3 digit numbers. It will ignore any matches that are preceded by a
    "don't()" pattern and only start matching once a "do()" pattern appears. For each valid match,
    it multiplies the numbers and then sums up the results of all multiplications.

    :param corrupted_memory: The input string potentially containing multiple occurrences of the
                             pattern "mul(X,Y)" and the "don't()" and "do()" patterns.
    :type corrupted_memory: str

    :return: The sum of the products of each pair of numbers found in the input string
    :rtype: int
    """

    # Initialize the sum of products
    total_sum = 0

    # Flag to track if we are in a "do" section
    do_mode = False

    # Regular expression to match mul(X,Y) patterns
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    # Regular expression to match "do()" and "don't()"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    # Iterate over all patterns in the string
    for match in re.finditer(f"{do_pattern}|{dont_pattern}|{mul_pattern}", corrupted_memory):
        # If it's a "do()" pattern, activate the "do_mode"
        if match.group(0) == "do()":
            do_mode = True
        # If it's a "don't()" pattern, deactivate the "do_mode"
        elif match.group(0) == "don't()":
            do_mode = False
        # If it's a "mul(X,Y)" pattern and we are in "do_mode", process it
        elif match.group(0).startswith("mul") and do_mode:
            num1, num2 = map(int, match.groups())  # Convert captured numbers to integers
            total_sum += num1 * num2

    return total_sum

def main():
    """
    Print answers to problems Part1 and Part2.
    """

    file_path = 'inputs/input_day_3.txt'
    corrupted_memory = load_input(file_path)
    answer_part_1 = part_1(corrupted_memory)
    answer_part_2 = part_2(corrupted_memory)

    print('Part 1:', answer_part_1)
    print('Part 2:', answer_part_2)

if __name__ == '__main__':
    main()
