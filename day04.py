from typing import Set


class BingoBoardElement:
    def __init__(self, x_pos, y_pos, value):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.value = value
        self.is_element_marked = False

    def mark_element(self):
        self.is_element_marked = True

class BingoBoard:
    def __init__(self, board_elements):
        self._board_elements = board_elements
        self._bingo_board = self._generate_bingo_board()

    def _generate_bingo_board(self):
        board_elements_parsed = [list(filter(lambda x: x != '', element.replace('\n','').split(' '))) for element in self._board_elements]
        bingo_board = []
        for pos_y in range(len(board_elements_parsed)):
            row = []
            for pos_x in range(len(board_elements_parsed[pos_y])):
                bingo_board_element = BingoBoardElement(pos_x, pos_y, board_elements_parsed[pos_y][pos_x])
                row.append(bingo_board_element)
            bingo_board.append(row)   
        return bingo_board
    
    def mark_bingo_element(self, value_to_mark):
        for row in self._bingo_board:
            for element in row: 
                if element.value == value_to_mark:
                    element.mark_element()

    def has_bingo(self):
        #look for bingo in rows
        for row in self._bingo_board:
            row_bingo_set = set(element.is_element_marked for element in row)
            if len(row_bingo_set) == 1 and row_bingo_set == {True}:
                return True

        #look for bingo in columns
        for row_idx in range(len(self._bingo_board)):
            col_bingo_set = set(self._bingo_board[col_idx][row_idx].is_element_marked for col_idx in range(len(self._bingo_board[row_idx])))
            if len(col_bingo_set) == 1 and col_bingo_set == {True}:
                return True
        return False

    def print_bingo_board(self):
        for row in self._bingo_board:
            print(row[0].value, row[0].is_element_marked, row[1].value, row[1].is_element_marked, row[2].value, row[2].is_element_marked, row[3].value, row[3].is_element_marked, row[4].value, row[4].is_element_marked)            

    def get_sum_of_unchecked(self):
        unchecked_sum = 0
        for row in self._bingo_board:
            for element in row:
                if not element.is_element_marked:
                    unchecked_sum += int(element.value)
        return unchecked_sum

class Day4:
    def __init__(self, calls, boards_elements):
        self._calls = calls
        self._boards_elements = boards_elements
        self._bingo_boards = [BingoBoard(board_elements=board_elements) for board_elements in self._boards_elements]
    
    def solve_part1(self):
        bingo_found = False
        solution = None
        for call in self._calls:
            for board in self._bingo_boards:
                board.mark_bingo_element(call)
                bingo_found = board.has_bingo()
                if bingo_found:
                    solution = board.get_sum_of_unchecked() * int(call)
                    break 
            if bingo_found:
                break
        return solution
    
    def solve_part2(self):
        board_to_win = None
        element = None
        for call in self._calls:
            for board in self._bingo_boards:
                if not board.has_bingo():
                    board.mark_bingo_element(call)
                    if board.has_bingo():
                        board_to_win = board
                        element = call
        return board_to_win.get_sum_of_unchecked() * int(element)


if __name__ == '__main__':

    with open('./inputs/d4_input_boards.txt') as f:
        boards_lines = list(filter(lambda x: x != '\n', f.readlines()))
        bingo_boards_elements = [boards_lines[line_idx:line_idx+5] for line_idx in range(0, len(boards_lines)-5, 5)]
    
    with open('./inputs/d4_input_numbers.txt') as f:
        calls = f.readlines()[0].split(',')
    
    # boards = [BingoBoard(board_elements=board_elements) for board_elements in bingo_boards_elements]
    # bingo_found = False
    
    # part1 
    # for call in calls:
    #     for board in boards:
    #         board.mark_bingo_element(call)
    #         bingo_found = board.has_bingo()
    #         if bingo_found:
    #             print(board.get_sum_of_unchecked() * int(call))
    #             break 
    #     if bingo_found:
    #         break
    
    # #part2
    # board_to_win = None
    # element = None
    # for call in calls:
    #     for board in boards:
    #         if not board.has_bingo():
    #             board.mark_bingo_element(call)
    #             if board.has_bingo():
    #                 board_to_win = board
    #                 element = call
    
    # print(board_to_win.get_sum_of_unchecked() * int(element))

    day4 = Day4(calls=calls, boards_elements=bingo_boards_elements)
    day4_part1_solution = day4.solve_part1()
    day4_part2_solution = day4.solve_part2()
    print(f'part 1 solution: {day4_part1_solution} \npart 2 solution: {day4_part2_solution}')






        