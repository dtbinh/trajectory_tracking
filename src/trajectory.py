#!/usr/bin/env python
import math

from geometry_msgs.msg import Point

from constants import SIMULATION_TIME_IN_SECONDS


def create_trajectory(trajectory_type):
    if trajectory_type == 'linear':
        return LinearTrajectory(0.05, 0, 0.05, 0)
    elif trajectory_type == 'circular':
        return CircularTrajectory(2.0, 120)
    elif trajectory_type == 'squared':
        return SquaredTrajectory(2.0, 0.25, 0.25)


class Trajectory:
    def get_position_at(self, t):
        pass


class LinearTrajectory(Trajectory):
    def __init__(self, v_x, x_0, v_y, y_0):
        self.v_x = v_x
        self.v_y = v_y
        self.x_0 = x_0
        self.y_0 = y_0

    def get_position_at(self, t):
        position = Point()
        position.x = self.v_x * t + self.x_0
        position.y = self.v_y * t + self.y_0

        return position

class CircularTrajectory(Trajectory):
    def __init__(self, radius, period):
        self.radius = radius
        self. period = period

    def get_position_at(self, t):
        position = Point()
        position.x = self.radius * math.cos(2 * math.pi * t / self.period)
        position.y = self.radius * math.sin(2 * math.pi * t / self.period)

        return position


class SquaredTrajectory(Trajectory):
    def __init__(self, side, x_0, y_0):
        self.side = side
        self.v = 4.0 * side / SIMULATION_TIME_IN_SECONDS
        self.x_0 = x_0
        self.y_0 = y_0

    def get_position_at(self, t):
        position = Point()

        if 0 <= t < SIMULATION_TIME_IN_SECONDS / 4:
            position.x = self.v * t + self.x_0
            position.y = self.y_0
        elif SIMULATION_TIME_IN_SECONDS / 4 <= t < SIMULATION_TIME_IN_SECONDS / 2:
            position.x = self.x_0 + self.side
            position.y = self.v * (t - SIMULATION_TIME_IN_SECONDS / 4) + self.y_0
        elif SIMULATION_TIME_IN_SECONDS / 2 <= t < 3 * SIMULATION_TIME_IN_SECONDS / 4:
            position.x = -self.v * (t - SIMULATION_TIME_IN_SECONDS / 2) + self.x_0 + self.side
            position.y = self.y_0 + self.side
        else:
            position.x = self.x_0
            position.y = -self.v * (t - 3 * SIMULATION_TIME_IN_SECONDS / 4) + self.y_0 + self.side

        return position