"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
from maze.maze import Maze, Coordinates
from maze.mazehat import MazeHat


def test_view_to_sensehat():
    mh = MazeHat()
    maze = [
        list('#######'),
        list(' ##### '),
        list('# # # #'),
        list('  SHFH '),
        list('# # # #'),
        list(' ##### '),
        list('#######'),
    ]
    view = Maze(maze, 7).view(Coordinates(6, 6))
    gold_view = [
        mh.wall, mh.wall, mh.wall, mh.wall, mh.wall, mh.wall, mh.wall, mh.empty,
        mh.empty, mh.wall, mh.wall, mh.wall, mh.wall, mh.wall, mh.empty, mh.empty,
        mh.wall, mh.empty, mh.wall, mh.empty, mh.wall, mh.empty, mh.wall, mh.empty,
        mh.empty, mh.empty, mh.start, mh.avatar, mh.finish, mh.hazard, mh.empty, mh.empty,
        mh.wall, mh.empty, mh.wall, mh.empty, mh.wall, mh.empty, mh.wall, mh.empty,
        mh.empty, mh.wall, mh.wall, mh.wall, mh.wall, mh.wall, mh.empty, mh.empty,
        mh.wall, mh.wall, mh.wall, mh.wall, mh.wall, mh.wall, mh.wall, mh.empty,
        mh.empty, mh.empty, mh.empty, mh.empty, mh.empty, mh.empty, mh.empty, mh.empty,
    ]

    mview = mh.view_to_sensehat(view)

    assert mview == gold_view
