"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
from maze.maze import Maze
from maze.mazehat import MazeHat


def test_start():
    mh = MazeHat()
    value = Maze.START
    color = mh.map_value(value)

    assert color == mh.start


def test_finish():
    mh = MazeHat()
    value = Maze.FINISH
    color = mh.map_value(value)

    assert color == mh.finish


def test_wall():
    mh = MazeHat()
    value = Maze.WALL
    color = mh.map_value(value)

    assert color == mh.wall


def test_hazard():
    mh = MazeHat()
    value = Maze.HAZARD
    color = mh.map_value(value)

    assert color == mh.hazard


def test_empty():
    mh = MazeHat()
    value = Maze.EMPTY
    color = mh.map_value(value)

    assert color == mh.empty


def test_other():
    mh = MazeHat()
    value = -1
    color = mh.map_value(value)

    assert color == mh.error
