from utils import limit


class Selector(object):

    DIRECTIONS = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
    }

    def __init__(self):
        self._table = None
        self._view = None
        self.position = (0, 0)

    def setup(self, table, view):
        self._table = table
        self._view = view

    def should_move(self, action):
        return action in self.DIRECTIONS.keys()

    def control_movement(self, action):
        di, dj = self.DIRECTIONS[action]
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

    def handle_input(self, action):
        if self.should_move(action):
            return self.control_movement(action)

        return self.control_selection(action)

    def control_selection(self, action):
        raise NotImplementedError()