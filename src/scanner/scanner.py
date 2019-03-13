import ply.lex as lex

literals = ['+', '-', '*', '/', '=', '<', '>', ':', '\'', ',', ';', '(', ')', '[', ']', '{', '}']

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'eye': 'EYE',
    'zeros': 'ZEROS',
    'ones': 'ONES',
    'print': 'PRINT',
    'for': 'FOR',
    'while': 'WHILE',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
}

tokens = ["REALNUM", "INTNUM", 'ID', 'STRING',
          "DOTADD", "DOTSUB", "DOTMUL", "DOTDIV",
          "ADDASSIGN", "SUBASSIGN", "MULASSIGN", "DIVASSIGN",
          "LEQ", "GEQ", "NOTEQ", "EQ",
          ] + list(reserved.values())

t_DOTADD = r'\.\+'
t_DOTSUB = r'\.-'
t_DOTMUL = r'\.\*'
t_DOTDIV = r'\./'
t_ADDASSIGN = r'\+='
t_SUBASSIGN = r'-='
t_MULASSIGN = r'\*='
t_DIVASSIGN = r'/='
t_LEQ = r'<='
t_GEQ = r'>='
t_NOTEQ = r'!='
t_EQ = r'=='

t_ignore = '  \t'


def t_ID(t):
    r'[A-Z]'
    return t


def t_INTNUM(t):
    r'\d+'
    t.value = int(t.value)
    return t


def T_REALNUM(t):
    r"([0-9]+)(\.)([0-9]+)?|(\.)([0-9]+)"
    t.value = float(t.value)
    return t


def t_COMMENT(t):
    r'\#.*'
    pass


def t_STRING(t):
    r"\"([^\\']+|\\'|\\\\)*\""
    t.value = t.value[1:-1]
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print
    "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)


def find_column(text, tok):
    line_start = text.rfind('\n', 0, tok.lexpos) + 1
    return (tok.lexpos - line_start) + 1


lexer = lex.lex()
