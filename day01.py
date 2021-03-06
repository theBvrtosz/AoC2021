
class Day1():

    def __init__(self, puzzle_input):
        self._puzzle_input = puzzle_input

    def _partirioned_sum(self, partition_width):
        curr = None
        prev = None
        increase_value_count = 0

        for pos in range(len(self._puzzle_input)):
            sublist = self._puzzle_input[pos:pos+partition_width]

            if len(sublist) == partition_width:
                curr = sum(sublist)
                if prev is not None: 
                    if curr > prev:
                        increase_value_count += 1
                prev = curr
        return increase_value_count

    def solve_part1(self):
        return self._partirioned_sum(1)    

    def solve_part2(self):
        return self._partirioned_sum(3)

if __name__ == '__main__':

    #open d1 puzzle input
    with open('./inputs/d1_input.txt') as f:
        d1_input = list(map(lambda x: int(x.replace('\n', '')), f.readlines()))

        day1 = Day1(d1_input)
        day1_part1_solution = day1.solve_part1()
        day1_part2_solution = day1.solve_part2()

        print(f'part 1 solution: {day1_part1_solution} \npart 2 solution: {day1_part2_solution}')
