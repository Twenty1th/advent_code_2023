def check_left(line: str, number_index: int) -> bool:
    number_index = number_index - 1 if number_index > 0 else number_index
    if line[number_index] != ".":
        return True


def check_right(line: str, number_index: int):
    number_index = number_index + 1 if number_index + 1 < len(line) else number_index
    if line[number_index] != ".":
        return True


def check_top_or_bot(line: str, from_number_index: int, to_number_index: int):
    from_number_index = to_number_index - 1 if from_number_index > 0 else from_number_index
    to_number_index = from_number_index + 1 if to_number_index + 1 < len(line) else to_number_index
    for i in line[from_number_index:to_number_index]:
        if i != ".":
            return True


def select_number_from_line(line: str) -> tuple[int, int, int]:
    numbers = []
    start_index = 0
    end_index = 0
    for j, i in enumerate(line):
        if i.isdigit():
            if start_index == 0:
                start_index = j
            if end_index <= j:
                end_index = j
            numbers.append(i)
            continue
        if numbers:
            yield int("".join(numbers)), start_index, end_index if numbers else None
            numbers = []
            start_index = 0
            end_index = 0


def _main(lines: list[str]):
    for i, line in enumerate(lines):
        preview_line = None
        next_line = None
        if i != 0:
            preview_line = lines[i - 1]
        if i + 1 != len(lines):
            next_line = lines[i + 1]
        for number, start_index, end_index in select_number_from_line(line):
            if any(
                    [
                        check_left(line, start_index),
                        check_right(line, end_index),
                        check_top_or_bot(preview_line, start_index, end_index) if preview_line else False,
                        check_top_or_bot(next_line, start_index, end_index) if next_line else False
                    ]
            ):
                print(number)
                yield number
            else:
                yield 0
    return 0


def main():
    pass


def test():
    with open("example.txt", 'r') as f:
        lines = f.readlines()
    print(sum(_main(lines)))


if __name__ == '__main__':
    # main()
    test()
