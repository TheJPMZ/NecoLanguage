# Precendece of operators found in https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap09.html#tag_09_04_08
OPERATORS = {"*": 2, "+": 2, "?": 2, ".": 1, "|": 0}
CHARACTERS = "abcdefghijklmnopqrstuvwxyz" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "0123456789" + "ε" + " "


def check_regex(regex: str) -> bool:
    """
    This function checks if the regex is valid
    :param regex: String
    :return: Boolean
    """
    error_stack = []

    if not regex or regex == "ε":
        error_stack.append("The regex is empty")
        raise ValueError(error_stack)

    if regex[0] in OPERATORS:
        error_stack.append("The regex cannot start with an operator (|, *, +, ?, .)")

    if regex[-1] in "|.":
        error_stack.append("The regex cannot end with | or .")

    if "(" in regex or ")" in regex:
        stack = []
        for i, j in enumerate(regex):
            if j == "(":
                stack.append(i)
            elif j == ")":
                if not stack:
                    error_stack.append(f"The regex contains an unopened parenthesis. (Index {i})")
                    break
                if regex[i - 1] == "(":
                    error_stack.append(f"The regex contains an empty parenthesis. (Index {stack[-1]})")
                    break
                stack.pop()
        if stack:
            error_stack.append(f"The regex contains an unclosed parenthesis. (Index {stack[-1]})")

    for index, char in enumerate(regex):
        if char not in CHARACTERS + "".join(OPERATORS.keys()) + "()":
            error_stack.append(f"The regex contains an invalid character '{char}' (Index {index})")

        if char in "*+?":
            if regex[index - 1] in OPERATORS:
                error_stack.append(f"The regex contains an operator before a quantifier. '{regex[index - 1]}{char}' (Index {index - 1})")

        if char in OPERATORS:
            if regex[index - 1] == char:
                error_stack.append(f"The regex contains two identical operators in a row. '{regex[index - 1]}{char}' (Index {index - 1})")

    if error_stack:
        raise ValueError(error_stack)

    return True


def transform(regex: str) -> str:
    """
    This function transforms implicit concatenation into explicit concatenation
    :param regex: String
    :return: String with explicit concatenation
    """

    new_regex = ""

    for index, char in enumerate(regex):

        if char in CHARACTERS + "(" and index != 0:
            if regex[index - 1] in CHARACTERS + ")" + "*+?":
                new_regex += "."
        new_regex += char

    return new_regex


def to_postfix(regex: str):
    """
    This function converts the regex into postfix notation
    :param regex: String
    :return: String in postfix notation
    """

    stack = []
    postfix = []

    for char in regex:

        if char in CHARACTERS:
            postfix.append(char)

        elif char == "(":
            stack.append(char)

        elif char == ")":
            while stack[-1] != "(":
                postfix.append(stack.pop())
            stack.pop()

        elif char in OPERATORS:
            while stack and stack[-1] != "(" and OPERATORS[char] <= OPERATORS[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(char)

    while stack:
        postfix.append(stack.pop())

    return "".join(postfix)
