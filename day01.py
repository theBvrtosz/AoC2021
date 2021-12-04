
class Day1():

    def __init__(self, puzzle_input):
        self._puzzle_input = puzzle_input

    def solve_part1(self):
        
        increase_value_count = 0

        for pos in range(1,len(self._puzzle_input)):
            curr = self._puzzle_input[pos]
            prev = self._puzzle_input[pos-1]

            if curr > prev: 
                increase_value_count += 1
        
        return increase_value_count
    

    def solve_part2(self):
        curr = None
        prev = None
        increase_value_count = 0

        for pos in range(len(self._puzzle_input)):
            sublist = self._puzzle_input[pos:pos+3]

            if len(sublist) == 3:
                curr = sum(sublist)
                if prev is not None: 
                    if curr > prev:
                        increase_value_count += 1
                prev = curr
        return increase_value_count 

if __name__ == '__main__':

    #open d1 puzzle input
    with open('./inputs/d1_input.txt') as f:
        d1_input = list(map(lambda x: int(x.replace('\n', '')), f.readlines()))


        test_input = [199,200,208,210,200,207,240,269,260,263]
        day1 = Day1(d1_input)
        day1_part1_solution = day1.solve_part1()
        day1_part2_solution = day1.solve_part2()
        print(f'part 1 solution: {day1_part1_solution} \npart 2 solution: {day1_part2_solution}')
        