
import sys

from ply import yacc

import scanner
from src.parser import Mparser
from src.AST import TreePrinter
from src.lab4 import TypeChecker

if __name__ == '__main__':
    TreePrinter()
    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "opers.m"
        file = open(filename, "r")
    except IOError:
        sys.exit(0)

    text = file.read()
    scanner = scanner.Scanner(text)
    parser = Mparser.MParser(scanner)
    parser = yacc.yacc(module=parser)
    program = parser.parse(text, lexer=scanner.lexer)
    # print(program.printTree())
    typeChecker = TypeChecker()
    typeChecker.visit(program)  # or alternatively ast.accept(typeChecker)
    # if not typeChecker.errors:
    #    program.accept(Interpreter())
