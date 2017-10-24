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