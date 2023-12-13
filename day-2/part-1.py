THRESHOLD = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def split_line_to_game_num_and_sub_games(line: str) -> tuple[int, str]:
    game_num_str, sub_games = line.strip().split(": ")  # type: (str, str)
    game_num = int(game_num_str.split(" ")[-1])
    return game_num, sub_games


def split_str_sub_games_to_list(sub_games: str) -> list[str]:
    return sub_games.split("; ")


def sub_game_have_correct_cubes_num(sub_game: str) -> bool:
    list_of_cubes_count_with_name = sub_game.split(", ")
    for cube_count_with_name in list_of_cubes_count_with_name:
        count, name = cube_count_with_name.split(" ")  # type: (str, str)
        if THRESHOLD[name] < int(count):
            return False
    else:
        return True


def _main(line: str):
    game_num, sub_games = split_line_to_game_num_and_sub_games(line)
    sub_games = split_str_sub_games_to_list(sub_games)
    for sub_game in sub_games:
        if not sub_game_have_correct_cubes_num(sub_game):
            return 0
    else:
        return game_num


def main():
    with open("../day-2/example", 'r') as f:
        lines = f.readlines()
    print(sum([_main(line) for line in lines]))


def test():
    with open("../day-2/example", 'r') as f:
        lines = f.readlines()
    game_num = _main(lines[0])
    print(game_num)


if __name__ == '__main__':
    # test()
    main()
