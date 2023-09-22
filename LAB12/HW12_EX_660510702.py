#!/usr/bin/env python3 
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW12_EX
# 204111 Sec 002

def my_id():
    return "660510702"

def main():
    while True:
        x = int(input())
        print(xmas_tree(x)) 

def xmas_tree(n):
    
    tree = ""
    if n < 1:
        return ""

    tree += (" "*(n+4)) + ("|\n")
    tree += (" "*(n+2)) + ("--*--\n")
    tree += (" "*(n+3)) + ("/|\\\n")
    tree += (" "*(n+2)) + ("/* *\\\n")

    for i in range(n):
        for a in range(3):
            tree += " "*(2-a)
            for _ in range(n-i-1):
                tree += (" ")

            tree += ("/")
            for _ in range(a+2+i):
                tree += ("* ")
            
            tree += ("*\\\n")

    tree += (" ")*(n+3) + ("|||\n")
    tree += ("_")*(n+3) + ("|||") + ("_")*(n+3) + ("\n")

    return tree    
    

if __name__ == "__main__":
    main()