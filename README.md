# aMAZEing SenseHat

Maze exploration for the Raspberry Pi SenseHat.

You are presented with a 7x7 top-down view of the maze, centered around
the intrepid adventurer (the yellow dot). Why not use the full 8x8
array of LEDs on the SenseHat? Because the adventurer would not be
centered.

The start square is a blue dot.
The finish square is a green dot.
hazards are a red dot.

Two interfaces for maze exploration are offered: the joystick and the
accelerometer.

## Running

To run aMAZEing SenseHat, from the command prompt, run
amazeing_sensehat.py with python3, with the maze file as an argument.
To use the accelerometer as the control, add a '-a' to the command.
Use '-h' to display the command argument help.

    $ python3 amazeing_sensehat.py [-a] [-j] [-h] <maze file>

## Maze Creation

Brush up on your ASCII art, because mazes are text files.

    ' ' = passable area.
    'S' = starting position.
    'F' = finish position.
    'H' = hazard.

    Everything else is a wall.

Example:

    ##############################
    #S                          H#
    ########### ############ #####
    #    #   ## #            #  F#
    # ##   #    ##############  ##
    # ###########      #######  ##
    #              H#           H#
    ##############################

Maze size is limited only by your attention span.

## Requirements

* Python 3.4 and greater.
* Numpy.
* Raspberry Pi.
* SenseHat.

## License

Copyright 2017, Andrew Lin.
All rights reserved.

This software is released under the BSD 3-clause license. See LICENSE.txt or
https://opensource.org/licenses/BSD-3-Clause for more information
