"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
import argparse
import time

import logging
from sense_hat import SenseHat

from maze.maze import Maze
from maze.mazehat import MazeHat


def parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument('maze', help='Path to maze file')
    parser.add_argument(
        '-j', '--joystick',
        dest='input',
        action='store_const',
        const='joystick',
        help='Use joystick'
    )
    parser.add_argument(
        '-s', '--sensors',
        dest='input',
        action='store_const',
        const='sensors',
        help='Use sensors'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='log to screen.'
    )
    parser.set_defaults(input='joystick')
    args = parser.parse_args()

    return args


def get_joystick(sensehat):
    """Get joystick input.

    Parses last valid event since last read.

    Args:
        sensehat (SenseHat)

    Returns:
        direction, pause
    """
    pause = .25  # seconds
    while True:
        events = sensehat.stick.get_events()
        for event in reversed(events):
            if event.action in ('pressed', 'held'):
                if event.direction == 'up':
                    logging.debug('Joystick: %s, dir: %s, pause: %s', event.direction, Maze.NORTH, pause)
                    return Maze.NORTH, pause
                elif event.direction == 'down':
                    logging.debug('Joystick: %s, dir: %s, pause: %s', event.direction, Maze.SOUTH, pause)
                    return Maze.SOUTH, pause
                elif event.direction == 'left':
                    logging.debug('Joystick: %s, dir: %s, pause: %s', event.direction, Maze.WEST, pause)
                    return Maze.WEST, pause
                elif event.direction == 'right':
                    logging.debug('Joystick: %s, dir: %s, pause: %s', event.direction, Maze.EAST, pause)
                    return Maze.EAST, pause

            time.sleep(0.1)


def angle_adjust(angle):
    """Adjust angle from sensehat range to game range.

    Args:
        angle (float): sensehat angle reading.

    Returns:
        float
    """
    if angle > 180.0:
        angle -= 360.0

    return angle


def get_tilt(sensehat):
    """Get sensor input.

    The greater the tilt, the shorter the pause.

    Args:
        sensehat (SenseHat)

    Returns:
        direction, pause
    """
    pause = 0.4
    threshold = 5.0  # degrees

    while True:
        # Pitch and roll in orientation are in the range [0.0, 360.0).
        orientation = sensehat.get_orientation()
        pitch = angle_adjust(orientation['pitch'])
        roll = angle_adjust(orientation['roll'])

        if abs(pitch) > abs(roll):
            direction = Maze.WEST if pitch > 0.0 else Maze.EAST
            logging.debug('Sensor: (p: %s, r: %s), dir: %s, pause: %s', pitch, roll, direction, pause)
            if abs(pitch) > threshold:
                break
        else:
            direction = Maze.SOUTH if roll > 0.0 else Maze.NORTH
            logging.debug('Sensor: (p: %s, r: %s), dir: %s, pause: %s', pitch, roll, direction, pause)
            if abs(roll) > threshold:
                break

        time.sleep(0.1)

    return direction, pause


def draw(sensehat, location, maze, mazehat):
    """Draw maze location on sensehat.

    Args:
        sensehat (SenseHat):
        location (Coordinates):
        maze (Maze):
        mazehat (MazeHat):
    """
    view = maze.view(location)
    sensehat_view = mazehat.view_to_sensehat(view)
    sensehat.set_pixels(sensehat_view)


def finish_animation(sensehat):
    """Finish animation.

    Args:
        sensehat (SenseHat):
    """
    x = (255, 255, 0)
    w = (255, 255, 255)
    o = (0, 0, 0)
    icon = [
        o, o, x, x, x, x, o, o,
        o, x, x, x, x, x, x, o,
        x, x, w, x, x, w, x, x,
        x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x,
        x, w, x, x, x, x, w, x,
        o, x, w, w, w, w, x, o,
        o, o, x, x, x, x, o, o,
    ]
    sensehat.set_pixels(icon)
    time.sleep(1.5)
    sensehat.clear()


def hazard_animation(sensehat):
    """Hazard animation.

    Args:
        sensehat (SenseHat):
    """
    def fade(pixel):
        delta = 10
        return [max(p - delta, 0) for p in pixel]

    # Fade to black.
    while True:
        time.sleep(0.05)
        pixels = sensehat.get_pixels()
        pixels = [fade(p) for p in pixels]
        sensehat.set_pixels(pixels)
        if all((lambda x: x == [0, 0, 0])(p) for p in pixels):
            break


def main():
    args = parse_command_line()
    if args.verbose:
        logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    get_input = get_joystick if args.input == 'joystick' else get_tilt
    maze = Maze.load_path(args.maze, 7)
    mazehat = MazeHat()
    sh = SenseHat()
    sh.low_light = True
    location = maze.start

    running = True
    while running:
        draw(sh, location, maze, mazehat)

        if location == maze.finish:
            logging.debug('Finish!')
            finish_animation(sh)
            break
        elif location in maze.hazards:
            logging.debug('Hazard!')
            hazard_animation(sh)
            get_joystick(sh)
            location = maze.start
        else:
            direction, pause = get_input(sh)
            location = maze.move(location, direction)
            time.sleep(pause)


if __name__ == '__main__':
    main()
