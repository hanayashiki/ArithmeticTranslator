class Lexer:
    char = '\0'
    token = ""
    num = 0x33333334
    symbol = ""
    src = None
    srcpos = 0

    def __init__(self, file):
        try:
            self.src = open(file, "r+")
        except Exception as e:
            print(e.__str__())

    def getchar(self):
        self.char = self.src.read(1)
        if self.char == "":
            #print ("EOF")
            self.char = "$"
        #print("getchar:" + self.char)
        self.srcpos += 1

    def retract(self):
        #print("backchar:" + self.char)
        self.srcpos -= 1
        self.src.seek(self.srcpos, 0)

    def getsym(self):
        self.token = ""
        self.getchar()
        while self.char == ' ' or self.char == '\t' or self.char == '\n':
            self.getchar()
        if self.char == "+":
            self.symbol = "ADD"
        elif self.char == "*":
            self.symbol = "MULT"
        elif self.char == "(":
            self.symbol = "LP"
        elif self.char == ")":
            self.symbol = "RP"
        elif self.char.isalpha():
            self.symbol = "ID"
            self.token += self.char
            self.getchar()
            while self.char.isalpha() or self.char.isdigit():
                self.token += self.char
                self.getchar()
            self.retract()
        elif self.char == "$":
            self.symbol = "EOF"
            self.token = ""
        else:
            raise Exception("Lexical Error", self.srcpos)

