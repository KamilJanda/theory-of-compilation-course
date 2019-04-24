import sys

import ply.yacc as yacc

from src.lab3 import Mparser
from src.lab3 import scanner
from src.lab4 import TypeChecker

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "resources/opers.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    text = file.read()
    scanner = scanner.Scanner(text)
    parser = Mparser.MParser(scanner)
    parser = yacc.yacc(module=parser)
    program = parser.parse(text, lexer=scanner.lexer)

    # Below code shows how to use visitor
    typeChecker = TypeChecker.TypeChecker()
    typeChecker.visit(program)  # or alternatively ast.accept(typeChecker)
