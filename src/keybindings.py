import curses

from vendor.enum import Enum


# ASCII number of the command.
CTRL_V = 22
ESC = 27


class Command(Enum):
    change_output = [ord('o')]
    change_selector = [ord('i')]
    clear_selection = [ord('d'), ESC]
    down = [ord('j'), curses.KEY_DOWN]
    enter = [ord('\n'), curses.KEY_ENTER]
    left = [ord('h'), curses.KEY_LEFT]
    print_text = [ord('p')]
    quit = [ord('q')]
    right = [ord('l'), curses.KEY_RIGHT]
    select = [ord(' '), ord('v')]
    select_column = [ord('c'), CTRL_V]
    up = [ord('k'), curses.KEY_UP]

    @classmethod
    def match(cls, command, ordinal):
        return any(filter(lambda x: x == ordinal, command.value))

    @classmethod
    def any_match(cls, commands, ordinal):
        for command in commands:
            if cls.match(command, ordinal):
                return True

        return False


ORDINAL_TO_COMMAND = {}
for command in Command:
    for value in command.value:
        ORDINAL_TO_COMMAND[value] = command

