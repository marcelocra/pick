import curses

from selectors.selector import Selector

from keybindings import Command
from utils import printstr


class SingleSelector(Selector):

    def __init__(self):
        super(SingleSelector, self).__init__()
        self._selection = None

    def draw(self, pad):
        self._selection = set(self._table.selection)
        self._table.draw(pad, self._flags_for)

    def _flags_for(self, p, content):
        flags = 0
        if p == self.position:
            flags |= curses.color_pair(2)
        elif p in self._selection:
            flags |= curses.A_REVERSE
        else:
            flags |= curses.color_pair(1)
        return flags

    def control_selection(self, ordinal):
        redraw_output = False

        if Command.match(Command.select, ordinal):
            self._table.toggle_select(self.position)
            redraw_output = True
        elif Command.match(Command.clear_selection, ordinal):
            self._table.clear_selection()
            redraw_output = True
        elif Command.match(Command.select_column, ordinal):
            _, j = self.position
            self._table.select_column(j)
            redraw_output = True
        return redraw_output

    def draw_instructions(self, pad):
        # TODO: Remove hard-coded dependency on next selector, see View class for details
        printstr(pad, "Single-selection", curses.color_pair(7))
        printstr(pad, "     [i] multi-selection                                               ", curses.color_pair(3))
        printstr(pad, "[arrows] move              [c] select column         [p] print current ", curses.color_pair(3))
        printstr(pad, " [space] (un)select cell   [d] clear selection   [enter] print and copy", curses.color_pair(3))
        printstr(pad, "                                                     [q] abort         ", curses.color_pair(3))

        printstr(pad)
