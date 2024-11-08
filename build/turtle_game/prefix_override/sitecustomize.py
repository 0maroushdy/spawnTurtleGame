import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/roushdy/torbedo/spawn_turtle_catch_game/spawnTurtleGame/install/turtle_game'
