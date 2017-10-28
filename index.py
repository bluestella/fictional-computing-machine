import sys
import lexer
import re

RESERVED = 'RESERVED'
INT      = 'INT'
ID       = 'ID'

token_exprs = [
    (r'[ \n\t]+',              None),
    (r'#[^\n]*',               None),
    (r'\[',                    RESERVED),
    (r'\]',                    RESERVED),
    (r'DSTR',                  RESERVED),
    (r'DINT',                  RESERVED),
    (r'WITH',                  RESERVED),
    (r'MODU',                  RESERVED),
    (r'PLUS',                  RESERVED),
    (r'MINUS',                 RESERVED),
    (r'TIMES',                 RESERVED),
    (r'DIVBY',                 RESERVED),
    (r'RAISE',                 RESERVED),
    (r'ROOT',                  RESERVED),
    (r'MEAN',                  RESERVED),
    (r'DIST',                  RESERVED),
    (r'AND',                   RESERVED),
    (r'GIVEME?',               RESERVED),
    (r'STORE',                 RESERVED),
    (r'GIVEYOU!!',             RESERVED),
    (r'GIVEYOU!',              RESERVED),
    (r'CREATE',                RESERVED),
    (r'RUPTURE',               RESERVED),
    (r'[0-9]+',                INT),
    (r'[A-Za-z][A-Za-z0-9_]*', ID),
]

def main():
    #This open input file.
    openFile()

def openFile():
        if len(sys.argv) != 2:
            usage()
        filename = sys.argv[1]
        text = open(filename).read()
        tokens = imp_lex(text)
        print tokens
        for token in tokens:
            print token


def imp_lex(characters):
    return lexer.lex(characters, token_exprs)


if __name__ == '__main__':
    main()
