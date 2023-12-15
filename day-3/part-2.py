table = {
    "*": [],  # start [line_idx, line_position_idx]
    "numbers": [],  # {number: [line_idx, line_position_start_idx, line_position_end_idx]}
}


def select_number_from_line(line: str) -> tuple[int, int, int]:
    numbers = []
    start_index = None
    end_index = 0
    for j, i in enumerate(line):
        if i.isdigit():
            if start_index is None:
                start_index = j
            if end_index <= j:
                end_index = j
            numbers.append(i)
            continue
        if numbers:
            yield int("".join(numbers)), start_index, end_index
            numbers = []
            start_index = None
            end_index = 0
    if numbers:
        yield int("".join(numbers)), start_index, end_index


def find_star_idx(line: str):
    line_len = len(line)
    i = 0
    while i < line_len:
        if line[i] == "*":
            yield i
        i += 1


def select_numbers_and_stars_from_lines(lines: list[str]):
    for k, line in enumerate(lines):  # type: (int, str)
        for number, start_index, end_index in select_number_from_line(line):
            table['numbers'].append([k, start_index, end_index, number])
        for idx in find_star_idx(line):
            table["*"].append([k, idx])


def main():
    with open("example.txt", 'r') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    select_numbers_and_stars_from_lines(lines)
    _finally = []
    for star_line_idx, star_idx in table["*"]:
        first_number = None
        second_number = None
        for number in table['numbers']:
            n = None
            if number[0] == star_line_idx and number[1] == star_idx + 1:
                n = number
            elif number[0] == star_line_idx and number[2] == star_idx - 1:
                n = number
            elif number[0] in [star_line_idx + 1, star_line_idx - 1]:  # BOT
                if star_idx in range(number[1] - 1, number[2] + 2):
                    n = number
            if n:
                if first_number is None:
                    first_number = number
                elif first_number is not None:
                    second_number = number
        if first_number and second_number:
            _finally.append(first_number[3] * second_number[3])
    print(sum(_finally))


if __name__ == '__main__':
    main()
