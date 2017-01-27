"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
import tempfile

import numpy as np

from maze.maze import Maze


def test_load_single_line():
    gold_maze = np.array(
        [
            [Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL]
        ]
    )

    with tempfile.NamedTemporaryFile(mode='w+') as f:
        f.write('#####')
        f.seek(0)
        view_size = 1

        maze = Maze.load_path(f.name, view_size)

    assert np.all(maze.maze == gold_maze)


def test_multi_line():
    gold_maze = np.array(
        [
            [Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL],
            [Maze.WALL, Maze.EMPTY, Maze.EMPTY, Maze.EMPTY, Maze.WALL],
            [Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL, Maze.WALL]
        ]
    )
    with tempfile.NamedTemporaryFile(mode='w+') as f:
        f.write(
            '#####\n'
            '#   #\n'
            '#####\n'
        )
        f.seek(0)
        view_size = 1

        maze = Maze.load_path(f.name, view_size)

    assert np.all(maze.maze == gold_maze)
