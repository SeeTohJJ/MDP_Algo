from enum import Enum


class Direction(int, Enum):
    NORTH = 0
    # NORTH_EAST = 1
    EAST = 2
    # SOUTH_EAST = 3
    SOUTH = 4
    # SOUTH_WEST = 5
    WEST = 6
    # NORTH_WEST = 7
    SKIP = 8

    def __int__(self):
        return self.value

    @staticmethod
    def rotation_cost(d1, d2):
        diff = abs(d1 - d2)
        return min(diff, 8 - diff)

MOVE_DIRECTION = [
    (1, 0, Direction.EAST),
    (-1, 0, Direction.WEST),
    (0, 1, Direction.NORTH),
    (0, -1, Direction.SOUTH),
    # (1, 1, Direction.NORTH_EAST),
    # (1, -1, Direction.SOUTH_EAST),
    # (-1, 1, Direction.NORTH_WEST),
    # (-1, -1, Direction.SOUTH_WEST)
]

TURN_FACTOR = 10

EXPANDED_CELL = 2 # for both agent and obstacles

WIDTH = 20
HEIGHT = 20

# JJ Originally 2000, reduce to speed up computation
ITERATIONS = 2000
TURN_RADIUS = 1

SAFE_COST = 1000 # the cost for the turn in case there is a chance that the robot is touch some obstacle
SCREENSHOT_COST = 50 # the cost for the place where the picture is taken