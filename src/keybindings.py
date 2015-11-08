#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
import os


DEFAULT_ACTION_TABLE = {
    'quit': [ord('q')],
    'change_selector': [ord('i')],
    'change_output': [ord('o')],
    'print': [ord('p')],
    'enter': [ord('\n'), curses.KEY_ENTER],
    'up': [curses.KEY_UP],
    'right': [curses.KEY_RIGHT],
    'down': [curses.KEY_DOWN],
    'left': [curses.KEY_LEFT],
}

VIM_ACTION_TABLE = {
    'quit': [ord('q')],
    'change_selector': [ord('i')],
    'change_output': [ord('o')],
    'print': [ord('p')],
    'enter': [ord('\n'), curses.KEY_ENTER],
    'up': [ord('k')],
    'right': [ord('l')],
    'down': [ord('j')],
    'left': [ord('h')],
}

if os.environ.get('PICK_KEYBINDING_MODE') == 'vim':
    ACTION_TABLE = VIM_ACTION_TABLE
else:
    ACTION_TABLE = DEFAULT_ACTION_TABLE


def check_action_ordinal(action, ordinal):
    """ Check if given **ordinal** is at least one of the expected ones for
        given **action**, by checking ACTION_TABLE.
    """
    return any(filter(lambda x: x == ordinal, ACTION_TABLE[action]))
