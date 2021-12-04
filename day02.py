
class Day2:

    def __init__(self, puzzle_input) -> None:
        self._puzzle_input = puzzle_input
        self._commands = self._parse_puzzle_input()
    
    def _parse_puzzle_input(self):
        commands = list(map(lambda x: x.split(' '), self._puzzle_input))
        commands = list(map(lambda x: tuple((x[0], int(x[1])*-1)) if x[0] == 'up' else tuple((x[0], int(x[1]))), commands))
        return commands

    def _get_depth_change(self):
        depth_change_list = filter(lambda x: x[0] in ['up', 'down'], self._commands)
        return sum(list(map(lambda x: x[1], depth_change_list)))
    
    def _get_horizontal_change(self):
        horizontal_change_list = filter(lambda x: x[0] == 'forward', self._commands)
        return sum(list(map(lambda x: x[1], horizontal_change_list)))

    def solve_part1(self):
        return self._get_depth_change() * self._get_horizontal_change()

    def solve_part2(self):
        aim = 0
        horizontal = 0
        depth = 0
        for direction, value in self._commands:
            if direction == 'forward': 
                horizontal += value
                depth += aim * value
            elif direction in ('down', 'up'):
                aim += value
        return horizontal * depth

if __name__ == '__main__':
    with open('./inputs/d2_input.txt') as f:
        d2_input = list(map(lambda x: x.replace('\n', ''), f.readlines()))
        day2 = Day2(d2_input)
        day2_part1_solution = day2.solve_part1()
        day2_part2_solution = day2.solve_part2()
        print(f'part 1 solution is {day2_part1_solution} \npart 2 solution is {day2_part2_solution}')
