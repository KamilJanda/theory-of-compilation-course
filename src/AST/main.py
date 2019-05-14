import sys

from ply import yacc

from src.parser import Mparser
from src.scanner import scanner

if __name__ == '__main__':
    # TreePrinter()
    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "resources/example1.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    text = file.read()
    scanner = scanner.Scanner(text)
    parser = Mparser.MParser(scanner)
    parser = yacc.yacc(module=parser)
    program = parser.parse(text, lexer=scanner.lexer)
    print(program.printTree())
