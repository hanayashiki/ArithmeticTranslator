from syntax import *
from lexer import *

if __name__ == '__main__':
    syntax_obj = Syntax()
    syntax_obj.lexer_obj = Lexer("test_texts/syntax_test1.txt")
    syntax_obj.lexer_obj.getsym()
    syntax_obj.expr()
    print(syntax_obj.tokener_obj.tkn2addr)

    syntax_obj = Syntax()
    syntax_obj.lexer_obj = Lexer("test_texts/syntax_test2.txt")
    syntax_obj.lexer_obj.getsym()
    syntax_obj.expr()
    print(syntax_obj.tokener_obj.tkn2addr)

    syntax_obj = Syntax()
    syntax_obj.lexer_obj = Lexer("test_texts/syntax_test3.txt")
    syntax_obj.lexer_obj.getsym()
    syntax_obj.expr()
    print(syntax_obj.tokener_obj.tkn2addr)

