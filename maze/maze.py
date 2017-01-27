"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
from collections import namedtuple

import numpy as np

Coordinates = namedtuple('Coordinates', 'row column')


class Maze:
    """Beware the minotaur!"""
    EMPTY = 0
    WALL = 1
    START = 2
    FINISH = 3
    HAZARD = 4

    # Directions
    NORTH = 'north'
    SOUTH = 'south'
    EAST = 'east'
    WEST = 'west'

    def __init__(self, maze, view_size):
        """
        Args:
            maze (list): Maze as a list.
            view_size (int): edge length of view square.
        """
        self.view_radius = view_size // 2
        self.maze, self.start, self.finish, self.hazards = self.convert(maze)

    @classmethod
    def load(cls, f, view_size):
        """Load maze from file.

        Args:
            f (file): file to read from.
            view_size (int):

        Returns:
            Maze
        """
        maze = [list(l.strip()) for l in f]
        return cls(maze, view_size)

    @classmethod
    def load_path(cls, path, view_size):
        """Load maze from file path.

        Args:
            path (str): path to maze file.
            view_size (int):

        Returns:
            Maze
        """
        with open(path, 'r') as f:
            return cls.load(f, view_size)

    def convert(self, maze):
        """Convert maze-as-list to maze-as-numpy-ndarray.

        Args:
            maze (list):

        Returns:
            npmaze (np.ndarray),
            start (Coordinates),
            finish (Coordinates),
            hazards (list of Coordinates)
        """
        start = finish = None
        hazards = []

        radius = self.view_radius
        numeric_maze = []
        for ridx, r in enumerate(maze, radius):
            row = [self.EMPTY] * radius
            for cidx, c in enumerate(r, radius):
                if c == 'S':
                    start = Coordinates(ridx, cidx)
                    row.append(self.START)
                elif c == 'F':
                    finish = Coordinates(ridx, cidx)
                    row.append(self.FINISH)
                elif c == 'H':
                    hazards.append(Coordinates(ridx, cidx))
                    row.append(self.HAZARD)
                elif c == ' ':
                    row.append(self.EMPTY)
                else:
                    row.append(self.WALL)

            row += [self.EMPTY] * radius
            numeric_maze.append(row)

        maze_width = max((lambda x: len(x))(r) for r in numeric_maze)
        for r in numeric_maze:
            row_len = len(r)
            if row_len < maze_width:
                r += [self.EMPTY] * (maze_width - row_len)

        if radius > 0:
            numeric_maze = (
                [[self.EMPTY] * maze_width for _ in range(radius)] +
                numeric_maze
            )
            numeric_maze += [[self.EMPTY] * maze_width for _ in range(radius)]

        return np.array(numeric_maze), start, finish, hazards

    def view(self, location):
        """Returns current view in maze.

        Args:
            location (Coordinates): location in maze.

        Returns:
            np.ndarray
        """
        radius = self.view_radius
        v = self.maze[
            location.row - radius:location.row + radius + 1,
            location.column - radius:location.column + radius + 1
        ]
        return v

    def move(self, current_location, direction):
        """Move in maze.

        Args:
            current_location (Coordinates):
            direction (str): 'north', 'south', 'west', 'east'.

        Returns:
            Coordinates
        """
        if direction == self.NORTH:
            loc = self.move_north(current_location)
        elif direction == self.SOUTH:
            loc = self.move_south(current_location)
        elif direction == self.WEST:
            loc = self.move_west(current_location)
        elif direction == self.EAST:
            loc = self.move_east(current_location)
        else:
            loc = current_location

        return loc

    def move_north(self, current_location):
        new = current_location.row - 1
        if new < 0 or self.maze[new, current_location.column] == self.WALL:
            return current_location

        return Coordinates(new, current_location.column)

    def move_south(self, current_location):
        new = current_location.row + 1
        if (
            new >= self.maze.shape[0] or
            self.maze[new, current_location.column] == self.WALL
        ):
            return current_location

        return Coordinates(new, current_location.column)

    def move_west(self, current_location):
        new = current_location.column - 1
        if new < 0 or self.maze[current_location.row, new] == self.WALL:
            return current_location

        return Coordinates(current_location.row, new)

    def move_east(self, current_location):
        new = current_location.column + 1
        if (
            new >= self.maze.shape[1] or
            self.maze[current_location.row, new] == self.WALL
        ):
            return current_location

        return Coordinates(current_location.row, new)
