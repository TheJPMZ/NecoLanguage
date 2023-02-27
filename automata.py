import graphviz

class Automata:

    def __init__(self, initial: str, final: list[str], ttable: dict) -> None:
        self.initial = initial
        self.final = final
        self.ttable = ttable

        self.alphabet = []
        self.set_alphabet()

        self.states = []
        self.set_states()

        self.hasEpsilon = False

    def set_alphabet(self, alphabet: list[str] = None):
        if alphabet is None:
            self.alphabet = list(set([x for y in self.ttable.values() for x in y.keys()]))
        else:
            self.alphabet = alphabet

    def set_states(self, states: list[str] = None):
        if states is None:
            self.states = list(set([x for y in self.ttable.keys() for x in y])) + self.final
        else:
            self.states = states

    def __str__(self) -> str:
        header_list = self.alphabet
        divisor = len(str(self.initial)) + 2

        def text_format(text, filler=" "):
            return str(text).center(divisor, filler)

        string = text_format("", "_")

        for x in header_list:
            string += "|" + text_format(x, "_")

        string += "\n"

        for x in self.states:
            line = (str("*" if x in self.final else ">" if x == self.initial else "") + str(x)).rjust(divisor, " ")

            values = self.ttable[x] if x in self.ttable else []

            for header in header_list:
                line += "|" + text_format(values[header] if header in values else " ")
            string += line + "\n"

        return string

    def export(self, filename: str = "output"):

        with open(filename.join(("", ".gv")), "w", encoding="utf-8") as file:
            file.write("digraph finite_state_machine {\n    rankdir=LR;\n\n\t")
            file.write("node [shape = point]; Start;\n\t")
            file.write(f"node [shape = doublecircle]; {', '.join(self.final)};\n\t")
            file.write("node [shape = circle];\n\n\t")

            file.write(f"Start -> {self.initial}\n\n")

            for state, t_tbl in self.ttable.items():
                for trans, dest in t_tbl.items():
                    for single in dest if isinstance(dest, list) else [dest]:
                        file.write(f'\t{state} -> "{single}" [ label = "{trans}" ]\n')

            file.write("}")

        graphviz.render(engine="dot", format="png", filepath=filename.join(("", ".gv")))

        with open(filename.join(("", ".txt")), "w", encoding="utf-8") as file:
            file.write(f"Estados (Q): {self.states}\n")
            file.write(f"Alfabeto (∑): {[x for x in self.alphabet if x != 'ε']}\n")
            file.write(f"Inicial (q0): {self.initial}\n")
            file.write(f"Finales (F): {self.final}\n")
            file.write(f"Tabla de Transicion (δ):\n")
            file.write(str(self))
