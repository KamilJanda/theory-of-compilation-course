from src.AST import AST

indent_char = '| '


def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func

    return decorator


class TreePrinter:
    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.Program)
    def printTree(self, indent=0):
        print("Program\n")
        result = ""
        result += self.instructions.printTree(indent)
        return result

    @addToClass(AST.Instructions)
    def printTree(self, indent=0):
        print("Instructions\n")
        result = ""
        for i in self.instructions:
            result += i.printTree(indent)
        return result

    @addToClass(AST.ContinueInstruction)
    def printTree(self, indent=0):
        print("ContinueInstruction\n")
        return indent * indent_char + "CONTINUE\n"

    @addToClass(AST.BreakInstruction)
    def printTree(self, indent=0):
        print("BreakInstruction\n")
        return indent * indent_char + "BREAK\n"

    @addToClass(AST.Constant)
    def printTree(self, indent=0):
        print("Constant\n")
        result = indent * indent_char
        result += str(self.value)
        return result + "\n"

    @addToClass(AST.Variable)
    def printTree(self, indent=0):
        print("Variable\n")
        result = indent * indent_char
        result += self.name + '\n'
        return result

    @addToClass(AST.Assignment)
    def printTree(self, indent=0):
        print("Assignment\n")
        result = indent * indent_char + "=\n"
        result += self.variable.printTree(indent + 1)
        result += self.expression.printTree(indent + 1)
        return result

    @addToClass(AST.MatrixElement)
    def printTree(self, indent=0):
        print("MatrixElement\n")
        result = indent_char * indent + "REF\n"
        result += indent_char * (indent + 1) + self.variable + '\n'
        result += self.row.printTree(indent + 1)
        result += self.column.printTree(indent + 1)
        return result

    @addToClass(AST.ZerosInitialization)
    def printTree(self, indent=0):
        print("ZerosInitialization\n")
        result = indent_char * indent
        result += 'ZEROS\n'
        result += self.expression.printTree(indent + 1)
        return result

    @addToClass(AST.EyeInitialization)
    def printTree(self, indent=0):
        print("EyeInitialization\n")
        result = indent_char * indent
        result += 'EYE\n'
        result += self.expression.printTree(indent + 1)
        return result

    @addToClass(AST.OnesInitialization)
    def printTree(self, indent=0):
        print("OnesInitialization\n")
        result = indent_char * indent
        result += 'ONES\n'
        result += self.expression.printTree(indent + 1)
        return result

    @addToClass(AST.Reference)
    def printTree(self, indent=0):
        result = indent_char * indent + "REF\n"
        result += self.name.printTree(indent + 1)
        for c in self.coords:
            result += c.printTree(indent + 1)
        return result

    @addToClass(AST.Vector)
    def printTree(self, indent=0):
        print("Vector\n")
        result = indent * indent_char + "VECTOR\n"
        for e in self.elements:
            result += e.printTree(indent + 1)
        return result

    @addToClass(AST.MatrixAssignment)
    def printTree(self, indent=0):
        print("MatrixAssignment\n")
        result = indent * indent_char + "=\n"
        result += indent_char * (indent + 1) + self.variable.printTree()
        result += self.expression_list.printTree(indent + 1)
        return result

    @addToClass(AST.ListsOfExpressions)
    def printTree(self, indent=0):
        print("ListsOfExpressions\n")
        result = indent * indent_char + "LISTS\n"
        for e in self.expression_lists:
            result += e.printTree(indent + 1)
        return result

    @addToClass(AST.ListOfExpressions)
    def printTree(self, indent=0):
        print("ListOfExpressions\n")
        # result = indent * indent_char + "LIST\n"
        result = 0 * indent_char
        for e in self.expression_list:
            result += e.printTree(indent)
        return result

    @addToClass(AST.NegUnaryExpression)
    def printTree(self, indent=0):
        print("NegUnaryExpression\n")
        result = indent_char * indent
        result += "-" + '\n'
        result += self.expression.printTree(indent + 1)
        return result

    @addToClass(AST.TransUnaryExpression)
    def printTree(self, indent=0):
        print("TransUnaryExpression\n")
        result = indent_char * indent
        result += "TRANSPOSE" + '\n'
        result += self.expression.printTree(indent + 1)
        return result

    @addToClass(AST.BinaryExpression)
    def printTree(self, indent=0):
        print("BinaryExpression\n")
        result = indent_char * indent
        result += self.operator + '\n'
        result += self.expression_left.printTree(indent + 1)
        result += self.expression_right.printTree(indent + 1)
        return result

    @addToClass(AST.CompoundAssignment)
    def printTree(self, indent=0):
        print("CompoundAssignment\n")
        result = indent * indent_char + self.operator + "\n"
        result += indent_char * (indent + 1) + self.variable.printTree()
        result += self.expression.printTree(indent + 1)
        return result

    @addToClass(AST.ForInstruction)
    def printTree(self, indent=0):
        print("ForInstruction\n")
        result = indent * indent_char + "FOR\n"
        result += indent_char * (indent + 1) + self.variable.printTree()
        result += indent_char * (indent + 1) + "RANGE\n"
        result += self.start.printTree(indent + 2)
        result += self.end.printTree(indent + 2)
        result += self.instruction.printTree(indent + 1)
        return result

    @addToClass(AST.CompoundInstruction)
    def printTree(self, indent=0):
        print("CompoundInstruction\n")
        result = self.instructions.printTree(indent)
        return result

    @addToClass(AST.PrintInstructions)
    def printTree(self, indent=0):
        print("PrintInstructions\n")
        result = indent * indent_char + "PRINT\n"
        result += self.expressions_list.printTree(indent + 1)
        return result

    # przerzucic wyswietlanie
    @addToClass(AST.IfInstruction)
    def printTree(self, indent=0):
        print("IfInstruction\n")
        result = indent * indent_char + "IF\n"
        result += self.condition.printTree(indent + 1)
        result += indent * indent_char + "THEN\n"
        result += self.instruction.printTree(indent + 1)
        return result

    @addToClass(AST.IfElseInstruction)
    def printTree(self, indent=0):
        print("IfElseInstruction\n")
        result = indent * indent_char + "IF\n"
        result += self.condition.printTree(indent + 1)
        result += indent * indent_char + "THEN\n"
        result += self.instruction.printTree(indent + 1)
        result += indent * indent_char + "ELSE\n"
        result += self.else_instruction.printTree(indent + 1)
        return result

    @addToClass(AST.WhileInstruction)
    def printTree(self, indent=0):
        print("WhileInstruction\n")
        result = indent * indent_char + "WHILE\n"
        result += self.condition.printTree(indent + 1)
        result += self.instruction.printTree(indent + 1)
        return result

    @addToClass(AST.ReturnInstruction)
    def printTree(self, indent=0):
        print("ReturnInstruction\n")
        result = indent * indent_char + "RETURN\n"
        result += self.expression.printTree(indent + 1)
        return result
