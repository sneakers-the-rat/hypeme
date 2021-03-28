import builtins
import re
from random import randint, choice

_QUIETER = False
_LAST_PRINT = None

ESCAPE_CHARS = ('\n', '\r', '\t', '\b', '\f')


class Colors:
    # background colors with white text
    COMBOS = ['\033[1;4{col_ind}m'.format(col_ind=i) for i in range(1,7)]
    BOLD = '\033[1m'
    RESET = '\033[0m'

def _make_it_yell(in_string:str) -> str:
    """
    CAPITALIZE EVERYTHING EXCEPT ESCAPE SEQUENCES AND THEN MAKE IT COLORY
    """

    # strip any other ansi color codes present in the string
    in_string = re.sub(r'\x1b\[[0-9;]+m', '', in_string)

    # lil more cleanup
    in_string = in_string.lstrip("'").rstrip("'")

    # pick a color to start the out_string
    out_str = choice(Colors.COMBOS) + Colors.BOLD

    # iterate through string to capitalize!
    # this is super slow probs but waht do you want from a freaking novelty package
    for char in in_string:
        if char in ESCAPE_CHARS:
            out_str += char
            continue
        else:
            out_str += char.upper()

    # add some amount of exclaims
    out_str += "!"*randint(1, 10)

    # append color reset
    out_str += Colors.RESET

    return out_str


def _hype(printme, *args, **kwargs):
    """
    NO DOCS!!!!!! JUST HYPE!!!!!!!!!!!!
    """
    global _QUIETER
    global _LAST_PRINT

    # if just printing a newline, like ipython does for some reason,
    # just do it
    if isinstance(printme, str) and printme in ESCAPE_CHARS:
        builtins.ye_olde_print(printme, *args, **kwargs)
        return

    _LAST_PRINT = printme

    try:
        its_yelly_now = _make_it_yell(str(repr(printme)))
        builtins.ye_olde_print(its_yelly_now, *args, **kwargs)
    except:
        if _QUIETER:
            builtins.ye_olde_print(printme, *args, **kwargs)
        else:
            builtins.ye_olde_print("IF I CANT YELL IT THEN I WONT PRINT IT"+"!"*randint(10,100))

def relax():
    """
    ok sheesh i didnt mean anything by it i'll print whatever you want me to
    """
    global _QUIETER
    global _LAST_PRINT

    _QUIETER = True

    builtins.ye_olde_print("ok sorry i just get excited for you is all\n")
    builtins.ye_olde_print(_LAST_PRINT)

def no_hyping():
    """
    just tryin ta look out for ya! good luck and i'll catch up with u soon
    """
    builtins.ye_olde_print("smell ya later!")
    builtins.print = builtins.ye_olde_print


builtins.ye_olde_print = builtins.print
builtins.print = _hype