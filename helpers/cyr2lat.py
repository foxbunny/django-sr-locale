#!/usr/bin/env python
# coding=utf-8

import re
import codecs
from StringIO import StringIO
import sys

__VERSION__ = "0.0.1"

PAIRS = [
    (u'А', u'A'), 
    (u'Б', u'B'),
    (u'В', u'V'),
    (u'Г', u'G'),
    (u'Д', u'D'),
    (u'Ђ', u'Đ'),
    (u'Е', u'E'),
    (u'Ж', u'Ž'),
    (u'Z', u'Z'),
    (u'И', u'I'),
    (u'Ј', u'J'),
    (u'К', u'K'),
    (u'Л', u'L'),
    (u'Љ', u'Lj'),
    (u'М', u'M'),
    (u'Н', u'N'),
    (u'Њ', u'Nj'),
    (u'О', u'O'),
    (u'П', u'P'),
    (u'Р', u'R'),
    (u'С', u'S'),
    (u'Т', u'T'),
    (u'Ћ', u'Ć'),
    (u'У', u'U'),
    (u'Ф', u'F'),
    (u'Х', u'H'),
    (u'Ц', u'C'),
    (u'Ч', u'Č'),
    (u'Џ', u'Dž'),
    (u'Ш', u'Š'),
    (u'а', u'a'),
    (u'б', u'b'),
    (u'в', u'v'),
    (u'г', u'g'),
    (u'д', u'd'),
    (u'ђ', u'đ'),
    (u'е', u'e'),
    (u'ж', u'ž'),
    (u'з', u'z'),
    (u'и', u'i'),
    (u'ј', u'j'),
    (u'к', u'k'),
    (u'л', u'l'),
    (u'љ', u'lj'),
    (u'м', u'm'),
    (u'н', u'n'),
    (u'њ', u'nj'),
    (u'о', u'o'),
    (u'п', u'p'),
    (u'р', u'r'),
    (u'с', u's'),
    (u'т', u't'),
    (u'ћ', u'ć'),
    (u'у', u'u'),
    (u'ф', u'f'),
    (u'х', u'h'),
    (u'ц', u'c'),
    (u'ч', u'č'),
    (u'џ', u'dž'),
    (u'ш', u'š'),
    ]

def transliterate(str, transpairs):
    """Transliterate str based on transpairs pairs of strings
    
    `str` is a unicode string to be parsed.
    `transpairs` is a list of 2-tuples containing character pairs

    There is no need to prepend `(?u)` to the first character in a character
    pair, as this is done for you by `transliterate()`.

    """

    for pair in transpairs:
        sourcechar = u'(?u)' + pair[0]
        regexp = re.compile(sourcechar, re.UNICODE)
        str = regexp.sub(pair[1], str)
    return str

def printerror(error, code="Unknown"):
        print """
**************************************************************
ERROR (%s)
**************************************************************
%s
**************************************************************
""" % (code, error)


def printdocs(version=__VERSION__):
    print """
%s
==============================================================

cyr2lat.py %s

==============================================================

OVERVIEW
--------------------------------------------------------------
This script will take one or more UTF-8 encoded files, and 
transliterate all Serbian Cyrillic characters in those files
to matching Latin characters.

USAGE
--------------------------------------------------------------
To use this script, supply the name(s) of the file(s) to 
transliterate. The transliterated text will be printed out on 
stdout. If you want to save the results, we suggest you pipe 
the output into a file.

If multiple files are passed to this script, the results will
be concatenated!

EXAMPLE
--------------------------------------------------------------
$ python cyr2lat.py mytextfile.txt

==============================================================
""" % (version)


def main():
    try:
        arguments = sys.argv[1:] 
    except IndexError:
        printdocs()
        quit()
    for argument in arguments:
        cloaca = StringIO()
        for argument in arguments:
            try:
                infile = codecs.open(argument, 'r', 'utf-8')
            except IOError:
                printerror(error="""File `%s` does not exist or is not readable.
Please specify a valid file.""" % argument, code=2)
                quit(2)
            current = infile.read()
            infile.close()
            current = transliterate(current, PAIRS)
            cloaca.write(current)
        print cloaca.getvalue().encode("utf-8")
        cloaca.close()

if __name__ == "__main__":
    main()

