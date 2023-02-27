from regex import to_postfix, check_regex, transform
from automata import Automata


def thompson(regex: str):
    if not check_regex(regex):
        return None

    regex = transform(regex)
    postfix = to_postfix(regex)

    stack = []
    counter = 0

    def start_end(p_counter):
        new_start = str(p_counter)
        new_end = str(p_counter + 1)
        return new_start, new_end

    for char in postfix:
        if char == ".":
            right = stack.pop()
            left = stack.pop()

            transitions = {**left.ttable, **right.ttable}
            transitions.update({left.final[0]: {"ε": right.initial}})

            afn = Automata(left.initial, right.final, transitions)

            stack.append(afn)

        elif char == "|":
            start, end = start_end(counter)

            right = stack.pop()
            left = stack.pop()

            start_transitions = {start: {"ε": [left.initial, right.initial]}}
            end_transitions = {left.final[0]: {"ε": end}, right.final[0]: {"ε": end}}
            transitions = {**left.ttable, **right.ttable, **start_transitions, **end_transitions}

            afn = Automata(start, [end], transitions)

            stack.append(afn)

        elif char == "*":
            start, end = start_end(counter)

            right = stack.pop()

            start_transitions = {start: {"ε": [right.initial, end]}}
            end_transitions = {right.final[0]: {"ε": [right.initial, end]}}
            transitions = {**right.ttable, **start_transitions, **end_transitions}

            afn = Automata(start, [end], transitions)

            stack.append(afn)

        elif char == "+":
            start, end = start_end(counter)

            right = stack.pop()

            start_transitions = {start: {"ε": right.initial}}
            end_transitions = {right.final[0]: {"ε": [end, right.initial]}}
            transitions = {**right.ttable, **start_transitions, **end_transitions}

            afn = Automata(start, [end], transitions)

            stack.append(afn)
        elif char == "?":
            start, end = start_end(counter)

            right = stack.pop()

            start_transitions = {start: {"ε": [right.initial, end]}}
            end_transitions = {right.final[0]: {"ε": end}}
            transitions = {**right.ttable, **start_transitions, **end_transitions}

            afn = Automata(start, [end], transitions)

            stack.append(afn)
        else:
            start, end = start_end(counter)

            stack.append(Automata(start, [end], {start: {char: end}}))

        if char != ".":
            counter += 2

    return stack.pop()


if __name__ == "__main__":
    thompson("ab|c*").export()
