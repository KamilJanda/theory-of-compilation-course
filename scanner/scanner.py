import ply.lex as lex

tokens = (
    'ID',
    'DOTADD', 'DOTSUB', 'DOTMUL', 'DOTDIV',
    'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN',
    'EYE', 'ZEROS', 'ONES',
    'INTNUM', 'FLOATNUM'
)

literals = ['+', '-', '*', '/', '(', ')', '=']


def t_ID(t):
    r'[A-Z]'
    return t


t_ZEROS = r'zeros'


def t_INTNUM(t):
    r'\d+'
    t.value = int(t.value)
    return t


t_ignore = '  \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print
    "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)


def find_column(text, tok):
    return text.find(str(tok.value)) + 1


lexer = lex.lex()
