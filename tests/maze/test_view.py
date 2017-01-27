"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
import numpy as np

from maze.maze import Maze, Coordinates


def test_view_1():
    maze = [
        list('#####'),
        list('# # #'),
        list(' # # '),
        list('# # #'),
        list('#####')
    ]
    gold_view = np.array([[Maze.EMPTY]])
    m = Maze(maze, 1)
    location = Coordinates(2, 2)

    view = m.view(location)

    assert np.all(view == gold_view)


def test_view_3():
    maze = [
        list('#####'),
        list('# # #'),
        list(' # # '),
        list('# # #'),
        list('#####')
    ]
    gold_view = np.array(
        [
            [Maze.EMPTY, Maze.WALL, Maze.EMPTY],
            [Maze.WALL, Maze.EMPTY, Maze.WALL],
            [Maze.EMPTY, Maze.WALL, Maze.EMPTY],
        ]
    )
    m = Maze(maze, 3)
    location = Coordinates(3, 3)

    view = m.view(location)

    assert np.all(view == gold_view)


def test_view_5():
    maze = [
        list('#####'),
        list('# # #'),
        list(' # # '),
        list('# # #'),
        list('#####')
    ]
    gold_view = np.array(
        [
            [Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL],
            [Maze.WALL, Maze.EMPTY, Maze.WALL, Maze.EMPTY, Maze.WALL],
            [Maze.EMPTY, Maze.WALL, Maze.EMPTY, Maze.WALL, Maze.EMPTY],
            [Maze.WALL, Maze.EMPTY, Maze.WALL, Maze.EMPTY, Maze.WALL],
            [Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL],
        ]
    )
    m = Maze(maze, 5)
    location = Coordinates(4, 4)

    view = m.view(location)

    assert np.all(view == gold_view)
