from keybindings import Command, ORDINAL_TO_COMMAND
from utils import limit


class Selector(object):
    DIRECTIONS = {
        Command.up: (-1, 0),
        Command.down: (1, 0),
        Command.left: (0, -1),
        Command.right: (0, 1),
    }

    def __init__(self):
        self._table = None
        self._view = None
        self.position = (0, 0)

    def setup(self, table, view):
        self._table = table
        self._view = view

    def _should_move(self, ordinal):
        return Command.any_match(self.DIRECTIONS.keys(), ordinal)

    def control_movement(self, ordinal):
        di, dj = self.DIRECTIONS[ORDINAL_TO_COMMAND[ordinal]]
        i, j = self.position
        i = limit(i + di, 0, self._table.height - 1)
        j = limit(j + dj, 0, len(self._table.table[i]) - 1)
        self.position = (i, j)

        # Movement shouldn't trigger redraw of the output.
        return False

    def draw(self, pad):
        raise NotImplementedError()

    def draw_instructions(self, pad):
        pass

    def clear(self, pad):
        pass

    def handle_command(self, ordinal):
        if self._should_move(ordinal):
            return self.control_movement(ordinal)

        return self.control_selection(ordinal)

    def control_selection(self, action):
        raise NotImplementedError()
