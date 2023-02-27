from thompson import thompson as thompson


def main():
    thompson("ab*ab*").export("First")
    thompson("0?(1?)?0*").export("Second")
    thompson("(a*|b*)c").export("Third")
    thompson("(b|b)*abb(a|b)*").export("Fourth")
    thompson("(a|ε)b(a+)c?").export("Fifth")
    thompson("(a|b)*a(a|b)(a|b)").export("Sixth")


if __name__ == '__main__':
    main()
