#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

import pdb

class Remove_All_Adjacent_Duplicates_in_String_II():
    def removeDuplicates(self, s: str, k: int) -> str:
        lst  = lambda s, k: [s[i:i+k] for i in range(0,len(s)-k+1)]
        expr = re.compile(r'(.)\1{%d,}'%(k-1))
        
        ss = lst(s, k)
        rm = []
        for n, l in enumerate(ss):
            eval = expr.search(l)
            if eval:
                print(l)
                for i in range(k):
                    rm.append(n+i)
        
        result = []
        for i in range(len(ss)):
            if not (i in rm):
                result.append(ss[i])
        
        print(result)
        pdb.set_trace()

def main():
    s = 'lakkksklsllkjjlsjdsl'
    k = 2
    Remove_All_Adjacent_Duplicates_in_String_II().removeDuplicates(s, k)

if __name__ == '__main__':
    # cd /store/science/git/proyectos/leetcode/python/
    # ./medium.py
    main()