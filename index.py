import sys
import lexer
import re
import os


filetype = ".txt"
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


class Interpol:
    def main(self):
        #Get filename of sourcefile.
        if len(sys.argv) < 2:
            print ("Kindly add .ipol source file.")
            return
        
        src = self.__read_source_file(sys.argv[1])

        if src is None or len(src) < 1:
            print ("I don't see anything written. Write some codes. I'll interpret it for you.")
            return

        result = self.__parse_to_lexemes(src)
        print result

    def __parse_to_lexemes(self, characters):
        return lexer.lex(characters, token_exprs)

    def __read_source_file(self, filename):
        print(chr(9))
        if filename.endswith(filetype):
            if(os.path.exists(filename)):
                fileObj =  open(filename).read()
                return fileObj
                #return fileObj.read().splitlines()
            else:
                print("It seems " + filename + " does not exists!")
        else:
            print("Your filetype seems invalid. Interpol interpreter only accepts .ipol files.")
         return None


    

interpol = Interpol()
interpol.main()