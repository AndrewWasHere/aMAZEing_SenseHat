"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
from maze.maze import Maze, Coordinates


def test_unimpeded():
    maze = [
        list('#####'),
        list('   #'),
        list('   #')
    ]
    m = Maze(maze, 1)

    loc = Coordinates(1, 1)
    new_loc = m.move_east(loc)

    assert new_loc == Coordinates(loc.row, loc.column + 1)


def test_impeded():
    maze = [
        list('#####'),
        list('   #'),
        list('   #')
    ]
    m = Maze(maze, 1)

    loc = Coordinates(1, 2)
    new_loc = m.move_east(loc)

    assert new_loc == loc
