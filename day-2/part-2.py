from functools import reduce
from operator import mul


def split_line_to_game_num_and_sub_games(line: str) -> tuple[int, str]:
    game_num_str, sub_games = line.strip().split(": ")  # type: (str, str)
    game_num = int(game_num_str.split(" ")[-1])
    return game_num, sub_games


def sub_game_have_correct_cubes_num(sub_games: str) -> int:
    sub_games = sub_games.split("; ")
    cubes_maximus: dict[str, list[int]] = {
        "red": [],
        "green": [],
        "blue": [],
    }

    for sub_game in sub_games:
        list_of_cubes_count_with_name = sub_game.split(", ")
        for cube_count_with_name in list_of_cubes_count_with_name:
            count, name = cube_count_with_name.split(" ")  # type: (str, str)
            cubes_maximus[name].append(int(count))
    print(cubes_maximus)
    return reduce(mul, [max(value) for value in cubes_maximus.values()])


def _main(line: str):
    game_num, sub_games = split_line_to_game_num_and_sub_games(line)
    return sub_game_have_correct_cubes_num(sub_games)


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
