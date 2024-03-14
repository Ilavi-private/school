class Colors:
    """
        Some colors are terminal-specific
    """

    class Fore:
        DEFAULT = '\033[39m'
        BLACK = '\033[0;30m'
        RED = '\033[0;31m'
        GREEN = '\033[0;32m'
        YELLOW = '\033[0;33m'
        BLUE = '\033[0;34m'
        PURPLE = '\033[0;35m'
        CYAN = '\033[0;36m'
        GRAY = '\033[0;37m'
        BRIGHT_BLACK = '\033[0;90m'
        BRIGHT_RED = '\033[0;91m'
        BRIGHT_GREEN = '\033[0;92m'
        BRIGHT_YELLOW = '\033[0;93m'
        BRIGHT_BLUE = '\033[0;94m'
        BRIGHT_PURPLE = '\033[0;95m'
        BRIGHT_CYAN = '\033[0;96m'
        BRIGHT_GRAY = '\033[0;97m'

    class Back:
        DEFAULT = '\033[49m'
        BLACK = '\033[0;40m'
        RED = '\033[0;41m'
        GREEN = '\033[0;42m'
        YELLOW = '\033[0;43m'
        BLUE = '\033[0;44m'
        PURPLE = '\033[0;45m'
        CYAN = '\033[0;46m'
        GRAY = '\033[0;47m'
        BRIGHT_BLACK = '\033[0;100m'
        BRIGHT_RED = '\033[0;101m'
        BRIGHT_GREEN = '\033[0;102m'
        BRIGHT_YELLOW = '\033[0;103m'
        BRIGHT_BLUE = '\033[0;104m'
        BRIGHT_PURPLE = '\033[0;105m'
        BRIGHT_CYAN = '\033[0;106m'
        BRIGHT_GRAY = '\033[0;107m'


class Decorations:
    """
    Some decorations are terminal-specific
    """
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    BOLD_ITALIC = BOLD + ITALIC
    UNDERLINE = '\033[4m'
    INVERTED = '\033[7m'
    STRIKETHROUGH = '\033[9m'
    BOLD_UNDERLINE = BOLD + UNDERLINE
    DIM = '\033[2m'
    BLINK = '\033[5m'
    INVISIBLE = '\033[8m'
    FRAME = '\033[51m'


def silly_print(*values: object,
                sep: str = None,
                end: str = None,
                fore: str = None,
                back: str = None,
                decoration: str = None) -> None:
    """
    Print with foreground or background color and text decoration.
    Use check_terminal_codes() to check which options are available.
    """
    if fore is not None and back is not None:
        raise Warning('Foreground and background override each other. '
                      'Only one should be specified')
    if fore is not None:
        print(fore, end='')
    if back is not None:
        print(back, end='')
    if decoration is not None:
        print(decoration, end='')
    print(*values, sep=sep, end=end)
    if decoration is not None or fore is not None or back is not None:
        print('\033[0m', end='')


def silly_order_print(*values: object,
                      sep: str = None,
                      end: str = None,
                      fore=None,
                      back=None,
                      decoration=None) -> None:
    """
    Prints the text with provided colors and decorations in order. Note that separator and
    ending are not affected.
    """
    if back is None:
        back = [None]
    if fore is None:
        fore = [None]
    if decoration is None:
        decoration = [None]
    current = 0
    for i, val in enumerate(values):
        for char in str(val):
            silly_print(
                char,
                sep='',
                end='',
                fore=fore[current % len(fore)],
                back=back[current % len(back)],
                decoration=decoration[current % len(decoration)]
            )
            current += 1
        if i != len(values) - 1:
            print(sep if sep is not None else ' ', end='')
    print(end=end)


def check_terminal_codes():
    """
    Prints all colors and decorations, so you can see which options are available in your terminal.
    """
    print('Checking terminal codes: \n')
    print(f'----- Foreground colors -----')
    attrs = [attr for attr in dir(Colors.Fore) if attr[0] != '_']
    for attr in attrs:
        print(getattr(Colors.Fore, attr) + attr + '\033[0m')
    print('\n\n----- Background colors -----')
    attrs = [attr for attr in dir(Colors.Back) if attr[0] != '_']
    for attr in attrs:
        print(getattr(Colors.Back, attr) + attr + '\033[0m')
    print('\n\n----- Text decorations -----')
    attrs = [attr for attr in dir(Decorations) if attr[0] != '_']
    for attr in attrs:
        print(getattr(Decorations, attr) + attr + '\033[0m')
