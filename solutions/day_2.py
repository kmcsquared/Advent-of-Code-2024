"""Advent of Code solution for day 2: Red-Nosed Reports"""

import numpy as np

def load_input(file_path):
    """
    Load reports, each of which consists of a list of numbers
    called levels that are separated by spaces.

    :return: _description_
    :rtype: _type_
    """

    reports = []

    with open(file_path, encoding='utf-8') as file_reports:
        for report in file_reports:
            levels = np.array([int(x) for x in report.split()])
            reports.append(levels)

    return reports

def part_1(reports):
    """
    Calculate the number of reports for which:
        - The levels are either all increasing or all decreasing.
        - Any two adjacent levels differ by at least one and at most three.

    :return: Number of safe reports
    :rtype: int
    """

    num_safe_reports = 0
    unsafe_reports = []

    for report in reports:
        is_safe_report = False

        # If levels are either all increasing or all decreasing
        if len(report) == len(np.unique(report)):
            sorted_levels = np.sort(report)
            if np.array_equal(report, sorted_levels) or np.array_equal(report, sorted_levels[::-1]):
                levels_1 = report[:-1]
                levels_2 = report[1:]
                adjacent_differences = np.abs(levels_1-levels_2)
                is_valid_difference = (adjacent_differences >= 1) & (adjacent_differences <= 3)
                is_safe_report = is_valid_difference.all()

        if not is_safe_report:
            unsafe_reports.append(report)
        else:
            num_safe_reports += 1

    return num_safe_reports, unsafe_reports

def part_2(num_safe_reports, unsafe_reports):
    """
    Calculate the number of reports for which:
        - The levels are either all increasing or all decreasing.
        - Any two adjacent levels differ by at least one and at most three.
        - Removing a single level from an unsafe report would satisfy the above conditions.

    :return: Number of safe reports
    :rtype: int
    """

    num_new_safe_reports = 0

    for report in unsafe_reports:
        is_safe_report = False

        # Remove one element at a time until report is proved safe or unsafe
        for idx in range(len(report)):
            new_report = np.concatenate([report[:idx], report[idx+1:]])

            # If levels are either all increasing or all decreasing
            if len(new_report) == len(np.unique(new_report)):
                sorted_levels = np.sort(new_report)
                if np.array_equal(new_report, sorted_levels) or np.array_equal(new_report, sorted_levels[::-1]):
                    # Any two adjacent levels differ by at least one and at most three
                    levels_1 = new_report[:-1]
                    levels_2 = new_report[1:]
                    adjacent_differences = np.abs(levels_1-levels_2)
                    is_valid_difference = (adjacent_differences >= 1) & (adjacent_differences <= 3)
                    is_safe_report = is_valid_difference.all()

            if is_safe_report:
                break

        num_new_safe_reports += int(is_safe_report)

    return num_safe_reports + num_new_safe_reports


def main():
    """
    Print answers to problems Part1 and Part2.
    """

    file_path = 'inputs/input_day_2.txt'
    reports = load_input(file_path)
    num_safe_reports_part_1, unsafe_reports = part_1(reports)
    num_safe_reports_part_2 = part_2(num_safe_reports_part_1, unsafe_reports)

    print('Part 1:', num_safe_reports_part_1)   # 220
    print('Part 2:', num_safe_reports_part_2)   # 296

if __name__ == '__main__':
    main()
