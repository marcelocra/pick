#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses


# ASCII number of the command.
CTRL_V = 22
ESC = 27

ACTION_TABLE = {
    curses.KEY_DOWN: 'down',
    curses.KEY_ENTER: 'enter',
    curses.KEY_LEFT: 'left',
    curses.KEY_RIGHT: 'right',
    curses.KEY_UP: 'up',
    ord('\n'): 'enter',
    ord('i'): 'change_selector',
    ord('o'): 'change_output',
    ord('p'): 'print',
    ord('q'): 'quit',
    ord('d'): 'clear_selection',
    ord(' '): 'select',
    ord('c'): 'select_column',

    # Keybindings for Vim mode. We support these alongside the others above,
    # which explains why there are repeated bindings.
    ord('v'): 'select',
    ord('h'): 'left',
    ord('j'): 'down',
    ord('k'): 'up',
    ord('l'): 'right',
    CTRL_V: 'select_column',
    ESC: 'clear_selection',
}


def action_for_ordinal(ordinal):
    return ACTION_TABLE.get(ordinal)
