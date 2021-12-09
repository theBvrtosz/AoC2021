import pandas as pd


class Day3:
    def __init__(self, puzzle_input):
        self._puzzle_input = puzzle_input

    def _get_input_df(self):
        puzzle_input_cols = [ f"pos_{pos}" for pos in range(len(self._puzzle_input[0]))]
        puzzle_input_df = pd.DataFrame(self._puzzle_input, columns=puzzle_input_cols)
        return puzzle_input_df

    def solve_part1(self):
        puzzle_input_df = self._get_input_df()
        puzzle_input_cols = puzzle_input_df.columns
        gamma_rate = ''
        epsilon_rate = ''
        for col in puzzle_input_cols:
            gamma_rate += puzzle_input_df[col].value_counts().idxmax()
            epsilon_rate += puzzle_input_df[col].value_counts().idxmin()
        return int(gamma_rate,2) * int(epsilon_rate,2)
    
    def solve_part2(self):
        # it can be done better, but i don't care 
        oxygen_generator_rating_df = self._get_input_df()
        co2_scrubber_rating_df = self._get_input_df()
        puzzle_input_cols = oxygen_generator_rating_df.columns

        for col in puzzle_input_cols:
            oxygen_generator_value_counts = oxygen_generator_rating_df[col].value_counts()
            oxygen_generator_filter_value = '1' if oxygen_generator_value_counts[0] == oxygen_generator_value_counts[1] else oxygen_generator_value_counts.idxmax()
            oxygen_generator_rating_df = oxygen_generator_rating_df[oxygen_generator_rating_df[col] == oxygen_generator_filter_value]
            if len(oxygen_generator_rating_df) == 1:
                break
        oxygen_generator_value = "".join(list(oxygen_generator_rating_df.iloc[0]))

        for col in puzzle_input_cols:
            co2_scrubber_value_counts = co2_scrubber_rating_df[col].value_counts()
            co2_scrubber_filter_value = '0' if co2_scrubber_value_counts[0] == co2_scrubber_value_counts[1] else co2_scrubber_value_counts.idxmin()
            co2_scrubber_rating_df = co2_scrubber_rating_df[co2_scrubber_rating_df[col] == co2_scrubber_filter_value]
            if len(co2_scrubber_rating_df) == 1:
                break
        co2_scrubber_value = "".join(list(co2_scrubber_rating_df.iloc[0]))

        return int(oxygen_generator_value, 2) * int(co2_scrubber_value, 2)


        


if __name__ == '__main__':
    with open('./inputs/d3_input.txt') as f:
        d3_input = list(map(lambda x: list(x.replace('\n', '')), f.readlines()))
        day3 = Day3(d3_input)
        day3_part1_solution = day3.solve_part1()
        day3_part2_solution = day3.solve_part2()

        print(f'part 1 solution: {day3_part1_solution} \npart 2 solution: {day3_part2_solution}')