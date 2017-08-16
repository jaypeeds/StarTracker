#!/usr/bin/env python3.5

from enum import Enum
class RunningState(Enum):
    STOPPED = 0
    RUNNING = 1
    PAUSED  = 2
