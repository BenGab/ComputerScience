from enum import Enum
from types import MappingProxyType
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt

from generic_search import Node, dfs, node_to_path

class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"

class MazeLocation(NamedTuple):
    row: int
    column: int

class Maze:
    def __init__(self, rows: int = 10, columns: int = 10, sparseness: float = 0.2, start: MazeLocation = MazeLocation(0, 0), goal: MazeLocation = MazeLocation(9, 9)) -> None:
        self.rows: int = rows
        self.colums: int = columns
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        self._randomly_fill(rows, columns, sparseness)
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL
    
    def _randomly_fill(self, rows: int, columns: int, sparseness: float):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED

    def goal_test(self, ml: MazeLocation) -> bool:
        return ml == self.goal

    def successors(self, ml: MazeLocation) -> List[MazeLocation]:
        locations: List[MazeLocation] = []

        if ml.row + 1 < self.rows and self._grid[ml.row + 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row + 1, ml.column))
        
        if ml.row - 1 >= 0 and self._grid[ml.row - 1][ml.column] !=  Cell.BLOCKED:
            locations.append(MazeLocation(ml.row - 1, ml.column))
        
        if ml.column + 1 < self.colums and self._grid[ml.row][ml.column + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column + 1))
        
        if ml.column - 1 >= 0 and self._grid[ml.row][ml.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column - 1))

        return locations
    
    def __str__(self) -> str:
        output: str = ""
        for row in self._grid:
            output += "".join([c.value for c in row]) + "\n"
        return output
    
    def mark(self, path: List[MazeLocation]) -> None:
        for location in path:
            self._grid[location.row][location.column] = Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL
    
    def clear(self, path: List[MazeLocation]) -> None:
        for location in path:
            self._grid[location.row][location.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

if __name__ == "__main__":
    maze: Maze = Maze()
    print(maze)
    solutionDfs: Optional[Node[MazeLocation]] = dfs(maze.start, maze.goal_test, maze.successors)
    if solutionDfs is None:
        print("No solution found with depth first search")
    else:
        pathDfs: List[MazeLocation] = node_to_path(solutionDfs)
        maze.mark(pathDfs)
        print(maze)
        maze.clear(pathDfs)