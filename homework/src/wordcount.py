# python3 -m homework data/input data/output

from homework.src._internals.parse_args import parse_args
from homework.src._internals.read_all_lines import read_all_lines


def main():
    input_folder, output_folder = parse_args()
    lines = read_all_lines(input_folder)

    print(f"Input Path: {input_folder}")
    print(f"Output Path: {output_folder}")
