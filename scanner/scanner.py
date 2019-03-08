import ply.lex as lex

tokens = (
    'ID',
    'ADD', 'SUB', 'MUL', 'DIV',
    'DOTADD', 'DOTSUB', 'DOTMUL', 'DOTDIV',
    '=', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN',
    'EYE', 'ZEROS', 'ONES'
)



def t_ID(t):
    r'[A-Z]'
    return t

def t_ZEROS(t):
    r'zeros\((\d+)\)'
    t.value = int(t.value)
    return t

lexer = lex.lex()
