#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

import pdb

class Remove_All_Adjacent_Duplicates_in_String_II():
    
    
    def removeDuplicates(self, s: str, k: int) -> str:
        expr = re.compile(r'(.)\1{%d,}'%(k-1))
        #
        i   = 0
        r   = ''
        end = 1
        pdb.set_trace()
        while end:
            end = 0
            i   = 0
            r   = ''
            while i < len(s):
                ss   = s[i:i+k]
                eval = expr.search(ss)
                if not eval:
                    r += ss[0]
                    i += 1
                else:
                    i   += k
                    end += 1
            s = r
            print(s)
        pdb.set_trace()

def main():
    s = 'ppkkkknopsstapttt'
    k = 3
    Remove_All_Adjacent_Duplicates_in_String_II().removeDuplicates(s, k)

if __name__ == '__main__':
    # cd /store/science/git/proyectos/leetcode/python/
    # ./medium.py
    main()