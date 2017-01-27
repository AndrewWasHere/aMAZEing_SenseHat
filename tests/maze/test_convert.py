"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
import numpy as np

from maze.maze import Maze, Coordinates


def test_minimum_view_size():
    maze = [
        list('#####'),
        list('#   #'),
        list('#####')
    ]
    gold_maze = np.array(
        [
            [Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL],
            [Maze.WALL, Maze.EMPTY, Maze.EMPTY, Maze.EMPTY, Maze.WALL],
            [Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL],
        ]
    )

    for view_size in range(2):
        np_maze, start, finish, hazards = Maze([''], view_size).convert(maze)
        assert np.all(np_maze == gold_maze)
        assert start is None
        assert finish is None
        assert hazards == []


def test_start():
    maze = [
        list('#####'),
        list('#S  #'),
        list('#####')
    ]
    gold_maze = np.array(
        [
            [Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL],
            [Maze.WALL, Maze.START, Maze.EMPTY, Maze.EMPTY, Maze.WALL],
            [Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL],
        ]
    )

    for view_size in range(2):
        np_maze, start, finish, hazards = Maze([''], view_size).convert(maze)
        assert np.all(np_maze == gold_maze)
        assert start == Coordinates(1, 1)
        assert finish is None
        assert hazards == []


def test_finish():
    maze = [
        list('#####'),
        list('#  F#'),
        list('#####')
    ]
    gold_maze = np.array(
        [
            [Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL],
            [Maze.WALL, Maze.EMPTY, Maze.EMPTY, Maze.FINISH, Maze.WALL],
            [Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL],
        ]
    )

    for view_size in range(2):
        np_maze, start, finish, hazards = Maze([''], view_size).convert(maze)
        assert np.all(np_maze == gold_maze)
        assert start is None
        assert finish == Coordinates(1, 3)
        assert hazards == []


def test_hazard():
    maze = [
        list('#####'),
        list('# H #'),
        list('#####')
    ]
    gold_maze = np.array(
        [
            [Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL],
            [Maze.WALL, Maze.EMPTY, Maze.HAZARD, Maze.EMPTY, Maze.WALL],
            [Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL],
        ]
    )

    for view_size in range(2):
        np_maze, start, finish, hazards = Maze([''], view_size).convert(maze)
        assert np.all(np_maze == gold_maze)
        assert start is None
        assert finish is None
        assert hazards == [Coordinates(1, 2)]


def test_view_size_edge():
    maze = [
        list('#####'),
        list('#   #'),
        list('#####')
    ]
    gold_maze = np.array(
        [
            [
                Maze.EMPTY, Maze.EMPTY, Maze.EMPTY, Maze.EMPTY, Maze.EMPTY,
                Maze.EMPTY, Maze.EMPTY
            ],
            [
                Maze.EMPTY, Maze.WALL,  Maze.WALL,  Maze.WALL,  Maze.WALL,
                Maze.WALL,  Maze.EMPTY
            ],
            [
                Maze.EMPTY, Maze.WALL,  Maze.EMPTY, Maze.EMPTY, Maze.EMPTY,
                Maze.WALL,  Maze.EMPTY
            ],
            [
                Maze.EMPTY, Maze.WALL,  Maze.WALL,  Maze.WALL,  Maze.WALL,
                Maze.WALL,  Maze.EMPTY
            ],
            [
                Maze.EMPTY, Maze.EMPTY, Maze.EMPTY, Maze.EMPTY, Maze.EMPTY,
                Maze.EMPTY, Maze.EMPTY
            ],
        ]
    )

    for view_size in range(2, 4):
        np_maze, start, finish, hazards = Maze([''], view_size).convert(maze)
        assert np.all(np_maze == gold_maze)
        assert start is None
        assert finish is None
        assert hazards == []


def test_steady_state():
    maze = [
        list('#####'),
        list('#   #'),
        list('#####')
    ]
    gold_maze = np.array(
        [
            [
                Maze.EMPTY, Maze.EMPTY, Maze.EMPTY, Maze.EMPTY, Maze.EMPTY,
                Maze.EMPTY, Maze.EMPTY, Maze.EMPTY, Maze.EMPTY
            ],
            [
                Maze.EMPTY, Maze.EMPTY, Maze.EMPTY, Maze.EMPTY, Maze.EMPTY,
                Maze.EMPTY, Maze.EMPTY, Maze.EMPTY, Maze.EMPTY
            ],
            [
                Maze.EMPTY, Maze.EMPTY, Maze.WALL,  Maze.WALL,  Maze.WALL,
                Maze.WALL,  Maze.WALL,  Maze.EMPTY, Maze.EMPTY
            ],
            [
                Maze.EMPTY, Maze.EMPTY, Maze.WALL,  Maze.EMPTY, Maze.EMPTY,
                Maze.EMPTY, Maze.WALL,  Maze.EMPTY, Maze.EMPTY
            ],
            [
                Maze.EMPTY, Maze.EMPTY, Maze.WALL,  Maze.WALL,  Maze.WALL,
                Maze.WALL,  Maze.WALL,  Maze.EMPTY, Maze.EMPTY
            ],
            [
                Maze.EMPTY, Maze.EMPTY, Maze.EMPTY, Maze.EMPTY, Maze.EMPTY,
                Maze.EMPTY, Maze.EMPTY, Maze.EMPTY, Maze.EMPTY
            ],
            [
                Maze.EMPTY, Maze.EMPTY, Maze.EMPTY, Maze.EMPTY, Maze.EMPTY,
                Maze.EMPTY, Maze.EMPTY, Maze.EMPTY, Maze.EMPTY
            ],
        ]
    )

    for view_size in range(4, 6):
        np_maze, start, finish, hazards = Maze([''], view_size).convert(maze)
        assert np.all(np_maze == gold_maze)
        assert start is None
        assert finish is None
        assert hazards == []
