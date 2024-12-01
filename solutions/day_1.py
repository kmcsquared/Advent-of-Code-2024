"""Advent of Code solution for day 1: Historian Hysteria """

import numpy as np

def load_input(filename):

    """
    Load lists of location IDs.

    :return: Lists of location IDs
    :rtype: list, list
    """

    # Store location IDs of each group
    location_ids_group_1 = []
    location_ids_group_2 = []

    # Get two location IDs per line
    with open(filename, encoding='utf-8') as file_location_ids:
        for line in file_location_ids:
            location_ids_current = line.split()
            location_ids_group_1.append(int(location_ids_current[0]))
            location_ids_group_2.append(int(location_ids_current[1]))

    # Sort the location IDs
    location_ids_group_1 = np.sort(np.array(location_ids_group_1))
    location_ids_group_2 = np.sort(np.array(location_ids_group_2))

    return location_ids_group_1, location_ids_group_2

def part_1(location_ids_group_1, location_ids_group_2):

    """
    Calculate the element-wise difference between two sets of numbers and return the sum of the
    differences.

    :return: Sum of element-wise differences between two sets of numbers
    :rtype: int
    """

    location_ids_group_1 = np.sort(np.array(location_ids_group_1))
    location_ids_group_2 = np.sort(np.array(location_ids_group_2))
    distances = np.abs(location_ids_group_1 - location_ids_group_2)
    sum_of_distances = distances.sum()

    return sum_of_distances

def part_2(location_ids_group_1, location_ids_group_2):
    """
    Calculate a total similarity score by adding up each number in the left list after multiplying
    it by the number of times that number appears in the right list.
    """

    unique, counts = np.unique(location_ids_group_2, return_counts=True)
    count_location_ids = dict(zip(unique, counts))
    similarity_score = 0

    for location_id in location_ids_group_1:
        if location_id in count_location_ids:
            similarity_score += location_id * count_location_ids[location_id]

    return similarity_score

def main():
    """
    Print answers to problems Part1 and Part2.
    """

    filename = 'inputs/input_day_1.txt'
    location_ids_group_1, location_ids_group_2 = load_input(filename)
    answer_part_1 = part_1(location_ids_group_1, location_ids_group_2)
    answer_part_2 = part_2(location_ids_group_1, location_ids_group_2)

    print('Part 1:', answer_part_1) # 1879048
    print('Part 2:', answer_part_2) # 21024792

if __name__ == '__main__':
    main()
