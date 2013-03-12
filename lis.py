# lis.py
# LISP-like lists, cons cells, etc
# Author: github.com/Sourceless

class cons:
    """A LISP-like cons cell, composed of two items."""
    def __init__(self, car, cdr=None):
        self.car = car
        self.cdr = cdr

    def __repr__(self):
        return "({car}, {cdr})".format(car=self.car, cdr=self.cdr)


def car(cons_cell):
    """Return the first element of a list/cons cell"""
    return cons_cell.car

def cdr(cons_cell):
    """Return the second element of a cons cell/tail of a list"""
    return cons_cell.cdr

def list(*items):
    """Constructs lists using cons cells as building blocks"""
    if len(items) == 1:
        return cons(items[0])
    return cons(items[0], list(*items[1:]))

def map(f, lst):
    """Apply a function to every item of a list"""
    if lst is None:
        return None
    return cons(f(car(lst)), map(f, cdr(lst)))

def foldl(f, lst, acc=0):
    """Left fold a list to a single value using a two-argument function"""
    if lst == None:
        return acc
    return foldl(f, cdr(lst), f(acc, car(lst))) # Nice and tail-recursive, too

def foldr(f, lst, acc=0):
    """Right fold a list given a two-argument function"""
    if cdr(lst) is not None:
        return f(car(lst), foldr(f, cdr(lst), acc))
    return f(car(lst), acc)
