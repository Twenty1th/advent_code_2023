table = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
}


def find_first_digit(line: str):
    _line = line
    max_tries = len(_line) * len(table)
    while max_tries >= 0:
        while len(_line) >= 1:
            for sub_number in table:
                if _line[0].isdigit():
                    first_number = _line[0]
                    return first_number
                elif _line.startswith(sub_number):
                    first_number = table[sub_number]
                    return first_number
            else:
                _line = _line[1:]
        _line = line
        max_tries = -1


def find_second_digit(line: str):
    _line = line[::-1]
    max_tries = len(_line) * len(table)
    while max_tries >= 0:
        while len(_line) >= 1:
            for sub_number in table:
                if _line[0].isdigit():
                    second_num = _line[0]
                    return second_num
                elif _line.startswith(sub_number[::-1]):
                    second_number = table[sub_number]
                    return second_number
            else:
                _line = _line[1:]
        _line = line
        max_tries = -1


def get_full_digit(line: str):
    line = line.strip()
    first_digit = find_first_digit(line)
    second_digit = find_second_digit(line)
    if all([first_digit, second_digit]):
        digit = int(f"{first_digit}{second_digit}")
        return digit
    return 0


def test():
    with open("../day-2/example", 'r') as f:
        lines = f.readlines()
    print(get_full_digit(lines[18]))


def main():
    with open("../day-2/example", 'r') as f:
        lines = f.readlines()
    print(sum([get_full_digit(line) for line in lines]))


if __name__ == '__main__':
    # test()
    main()
