from regex import to_postfix, check_regex, transform
from automata import Automata

def thompson(regex:str):

    if not check_regex(regex):
        return None

    regex = transform(regex)
    postfix = to_postfix(regex)

    stack = []
    counter = 0

    for char in postfix:
        if char == ".":
            pass
        elif char == "|":
            pass
        elif char == "*":
            pass
        elif char == "+":
            pass
        elif char == "?":
            pass
        else:
            inicio = str(counter)
            counter += 1
            end = str(counter)

            afn = Automata(inicio, [end], {inicio: {char: end}})
            stack.append(afn)