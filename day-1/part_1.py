def get_number_from_line(line: str):
    line_len = len(line)
    first_half, second_half = line[:line_len // 2], line[line_len // 2:]
    for i in first_half:
        if i.isdigit():
            first_num = int(i)
            break
    else:
        for i in second_half:
            if i.isdigit():
                first_num = int(i)
                break

    for i in second_half[::-1]:
        if i.isdigit():
            second_num = int(i)
            break
    else:
        for i in first_half[::-1]:
            if i.isdigit():
                second_num = int(i)
                break

    return int(f"{first_num}{second_num}")


def main():
    with open("example", 'r') as f:
        lines = f.readlines()

    print(sum([get_number_from_line(line) for line in lines]))


if __name__ == '__main__':
    main()
