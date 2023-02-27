from thompson import thompson as thompson

def menu():
    print("Menú")
    print("0. Ingresar expresión regular")
    print("1. (ab*ab*)")
    print("2. (0?(1?)?0*)")
    print("3. (a*|b*)c")
    print("4. (b|b)*abb(a|b)*")
    print("5. (a|ε)b(a+)c?")
    print("6. (a|b)*a(a|b)(a|b)")
    print("7. Salir")

def main():

    while True:
        menu()
        option = input("Ingrese una opción: \n>")
        if option == "0":
            regex = input("Ingrese la expresión regular: ")
            thompson(regex).export()
        elif option == "1":
            thompson("ab*ab*").export("First")
        elif option == "2":
            thompson("0?(1?)?0*").export("Second")
        elif option == "3":
            thompson("(a*|b*)c").export("Third")
        elif option == "4":
            thompson("(b|b)*abb(a|b)*").export("Fourth")
        elif option == "5":
            thompson("(a|ε)b(a+)c?").export("Fifth")
        elif option == "6":
            thompson("(a|b)*a(a|b)(a|b)").export("Sixth")
        else:
            break


if __name__ == '__main__':
    main()
