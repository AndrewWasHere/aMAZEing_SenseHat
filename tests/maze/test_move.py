"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
from unittest import mock

from maze.maze import Maze, Coordinates


def test_north():
    direction = Maze.NORTH
    maze = Maze([''], 1)
    location = Coordinates(0, 0)
    mock_loc = mock.MagicMock()

    with mock.patch.object(
        maze, 'move_north', return_value=mock_loc
    ) as mock_move:
        loc = maze.move(location, direction)

    assert mock_move.called
    assert loc == mock_loc


def test_south():
    direction = Maze.SOUTH
    maze = Maze([''], 1)
    location = Coordinates(0, 0)
    mock_loc = mock.MagicMock()

    with mock.patch.object(
        maze, 'move_south', return_value=mock_loc
    ) as mock_move:
        loc = maze.move(location, direction)

    assert mock_move.called
    assert loc == mock_loc


def test_west():
    direction = Maze.WEST
    maze = Maze([''], 1)
    location = Coordinates(0, 0)
    mock_loc = mock.MagicMock()

    with mock.patch.object(
        maze, 'move_west', return_value=mock_loc
    ) as mock_move:
        loc = maze.move(location, direction)

    assert mock_move.called
    assert loc == mock_loc


def test_east():
    direction = Maze.EAST
    maze = Maze([''], 1)
    location = Coordinates(0, 0)
    mock_loc = mock.MagicMock()

    with mock.patch.object(
        maze, 'move_east', return_value=mock_loc
    ) as mock_move:
        loc = maze.move(location, direction)

    assert mock_move.called
    assert loc == mock_loc


def test_other():
    direction = Maze.NORTH
    maze = Maze([''], 1)
    location = Coordinates(0, 0)

    new_loc = maze.move(location, direction)

    assert new_loc == location
