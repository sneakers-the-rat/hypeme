import builtins
from random import randint

_QUIETER = False
_LAST_PRINT = None

def _hype(printme):
    """
    NO DOCS!!!!!! JUST HYPE!!!!!!!!!!!!
    """
    global _QUIETER
    global _LAST_PRINT

    _LAST_PRINT = printme

    try:
        builtins.ye_olde_print(str(repr(printme)).upper().lstrip("'").rstrip("'") + "!"*randint(1, 10))
    except:
        if _QUIETER:
            builtins.ye_olde_print(printme)
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