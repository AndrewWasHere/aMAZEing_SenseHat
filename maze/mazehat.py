"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
from .maze import Maze


class MazeHat:
    """Convert Maze data to SenseHat data."""
    def __init__(
        self,
        start=(0, 0, 255),
        finish=(0, 255, 0),
        wall=(255, 255, 255),
        hazard=(255, 0, 0),
        avatar=(255, 255, 0),
    ):
        self.start = start
        self.finish = finish
        self.wall = wall
        self.hazard = hazard
        self.avatar = avatar
        self.empty = (0, 0, 0)
        self.error = (10, 10, 10)

    def view_to_sensehat(self, view):
        """View to sensehat values.

        Args:
            view (np.ndarray): 7x7 array.

        Returns:
            list
        """
        def matrix_iter(matrix):
            for r in matrix:
                for c in r:
                    yield c

        s_view = [[self.map_value(c) for c in r] for r in view.tolist()]
        s_view[3][3] = self.avatar
        for r in s_view:
            r.append(self.empty)

        s_view.append([self.empty] * 8)

        # s_view is an 8x8 array. But sensehat wants a linear array.
        s_view = [value for value in matrix_iter(s_view)]

        return s_view

    def map_value(self, v):
        """Convert view entry to sensehat value.

        Args:
            v (int): view value.

        Returns:
            tuple
        """
        if v == Maze.EMPTY:
            c = self.empty
        elif v == Maze.WALL:
            c = self.wall
        elif v == Maze.HAZARD:
            c = self.hazard
        elif v == Maze.FINISH:
            c = self.finish
        elif v == Maze.START:
            c = self.start
        else:
            # This should not happen.
            c = self.error

        return c
