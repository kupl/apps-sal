import ast

def to_postfix (infix):
    class PostFixVisitor(ast.NodeVisitor): 
        def visit_BinOp(self, node):
            self.visit(node.left)
            self.visit(node.right)
            self.visit(node.op)

        def visit_Num(self, node):
            postfix.append(str(node.n))
            
        def visit_Add(self, node):
            postfix.append('+')

        def visit_Sub(self, node):
            postfix.append('-')

        def visit_Mult(self, node):
            postfix.append('*')

        def visit_Div(self, node):
            postfix.append('/')

        def visit_Pow(self, node):
            postfix.append('^')

    postfix = []
    p = ast.parse(infix.replace('^', '**'))
    PostFixVisitor().visit(p)
    return ''.join(postfix)

