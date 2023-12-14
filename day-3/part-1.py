def check_left(line: str, number_index: int) -> bool:
    if number_index - 1 > 0 and line[number_index - 1] != ".":
        return True


def check_right(line: str, number_index: int):
    if number_index + 1 < len(line) and line[number_index + 1] != ".":
        return True


def check_top_or_bot(line: str, from_number_index: int, to_number_index: int):
    from_number_index = from_number_index - 1 if from_number_index > 0 else from_number_index
    for i in line[from_number_index:to_number_index + 2]:
        if i != "." and not i.isdigit():
            return True


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


def _main(lines: list[str]):
    for i, line in enumerate(lines):
        if i != 0:
            preview_line = lines[i - 1]
        else:
            preview_line = None
        if i + 1 < len(lines):
            next_line = lines[i + 1]
        else:
            next_line = None
        for number, start_index, end_index in select_number_from_line(line):
            if any(
                    [
                        check_left(line, start_index),
                        check_right(line, end_index),
                        check_top_or_bot(preview_line, start_index, end_index)
                        if preview_line else False,
                        check_top_or_bot(next_line, start_index, end_index)
                        if next_line else False
                    ]
            ):
                yield number


def main():
    with open("example.txt", 'r') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return [i for i in _main(lines)]


if __name__ == '__main__':
    m = main()
    print(sum(m))
