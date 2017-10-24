"""
DESIGN:

    1. syntax:
        expr -> term expr_tail
        expr_tail -> + term expr_tail
        expr_tail -> _
       trans:
        expr(output sym_self) -> term(output sym) expr_tail(input sym, output sym_self)
        expr_tail(input sym, output sym_self) -> + term(output sym') {new temp; ADD sym sym' temp} expr_tail(input temp, output sym_self)
        expr_tail(input sym, output sym_self) -> _ {sym_self = sym}

    2. syntax
        term -> fact term_tail
        term_tail -> * fact term_tail
        term_tail -> _
       trans:
        term(output sym_self) -> fact(output sym) term_tail(input sym, output sym_self)
        term_tail(input sym, output sym_self) -> * fact(output sym') {new temp; MULT sym sym' temp} term_tail(input temp, output sym_self)
        term_tail(input sym, output sym_self) -> _ {sym_self = sym}

    3. trans:
        fact(output sym) -> id(output token) {new sym; initialize sym with token}
        fact(output sym) -> ( expr(output sym) )

"""
from lexer import *
from symboller import *
from printer import *

class Syntax:
    lexer_obj = Lexer("text.txt")
    tokener_obj = Symboller()
    printer_obj = Printer()

    def __init__(self):
        self.tokener_obj = Symboller()
        self.printer_obj = Printer()

    def parse(self, file_addr):
        self.lexer_obj = Lexer(file_addr)
        self.lexer_obj.getsym()
        self.expr()

    def expr(self):
        sym = self.term()
        sym_self = self.expr_tail(sym)
        return sym_self

    def expr_tail(self, sym):
        if self.lexer_obj.symbol != "ADD":
            return sym
        else:
            self.lexer_obj.getsym()
            sym_ = self.term()
            temp = self.tokener_obj.new_sym("%TEMP")
            self.printer_obj.dump("ADD", sym, sym_, temp)
            sym_self = self.expr_tail(temp)
            return sym_self

    def term(self):
        #print("term begins")
        sym = self.fact()
        sym_self = self.term_tail(sym)
        return sym_self

    def term_tail(self, sym):
        if self.lexer_obj.symbol != "MULT":
            #print("term_tail_1 begins")
            return sym
        else:
            #print("term_tail_2 begins")
            self.lexer_obj.getsym()
            sym_ = self.fact()
            temp = self.tokener_obj.new_sym("%TEMP")
            self.printer_obj.dump("MULT", sym, sym_, temp)
            sym_self = self.term_tail(temp)
            return sym_self

    def fact(self):
        if self.lexer_obj.symbol == "ID":
            sym = self.tokener_obj.new_sym(self.lexer_obj.token)
            self.lexer_obj.getsym()
            return sym
        elif self.lexer_obj.symbol == "LP":
            self.lexer_obj.getsym()
            sym_self = self.expr()
            if self.lexer_obj.symbol != "RP":
                raise Exception("Syntax error", "missing )")
            self.lexer_obj.getsym()
            return sym_self
        else:
            raise Exception("Syntax error")
