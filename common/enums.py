from enum import Enum

class GameStatusEnum(Enum):
    IN_PROGRESS = 'IN_PROGRESS'
    DRAW = 'DRAW'
    X_WON = 'X_WON'
    O_WON = 'O_WON'
    INIT = 'INIT'