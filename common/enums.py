from enum import Enum

class GameStatusEnum(Enum):
    IN_PROGRESS = 'IN_PROGRESS'
    DRAW = 'DRAW'
    X_WON = 'X_WON'
    O_WON = 'O_WON'
    INIT = 'INIT'

class ExchangeNameEnum(Enum):
    GAME_EXCHANGE = 'game_exchange'
    CREATE_GAME = 'create_game'
    UPDATE_GAME = 'update_game'
    FIND_ONE_GAME = 'find_one_game'
    FIND_ALL_GAME  = 'find_all_game'

class RoutingKeyEnum(Enum):
    CREATE_GAME = 'create_game'
    UPDATE_GAME = 'update_game'
    FIND_ONE_GAME = 'find_one_game'
    FIND_ALL_GAME  = 'find_all_game'

class QueueNameEnum(Enum):
    DEFAULT_QUEUE = 'request_queue'