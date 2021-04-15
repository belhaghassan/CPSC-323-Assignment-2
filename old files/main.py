# ==========================================================================================================================
# Program Name: Lexical Analyzer
# Programming Language: Python 3
# Program Description: Takes in a source file with sample code and returns the tokenized version
# Program Files: main.py, functions.py, Lexer.py

# Author: Tommy, Bilal, Nicholas, Berkeley
# Group Name: Group-Uncle
# Institution: California State University, Fullerton
# Course: CPSC 323
# Section:
# Start Date: January, 2021
# Due Date: 07 March, 2021

# Copyright (C) 2021 
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License
# version 3 as published by the Free Software Foundation.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# Warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
# A copy of the GNU General Public License v3 is available here:  <https://www.gnu.org/licenses/>.
# ==========================================================================================================================

import Lexer as lexer
import syntax as syntax
import functions as func
import os
import sys

def printHeader():
  print("\nTOKENS\t\t\t\t\t Lexemes\n")
  return

def main():
  #Prompts user for source file and output file
  fileName = input("Please specify the name of the source file: ")
  fileOutput = input("Please specify a name for the output file: ")

  #Check to see if file exists
  if os.path.exists(fileName):
    sys.stdout = open(fileOutput,"w")
    print("Accessing file", fileName)
    printHeader()
    with open(fileName) as source:
        for row in source:
            if (not row.strip()):
                pass
            elif ((row.lstrip())[0] == '!'):
                pass
            else:
                #Separate the keywords and operators and add spaces
                row = func.separateElements(row)

                #Separate each string by space - i.e. "1, 2, 3" = {"1", ",", "2", ",", "3"}
                tokens = row.split()
                
                #Call lexer to analyze each token 
                lexer.lexer(tokens)

                syntax.syntax(row)
                
        return
  print("Invalid source file.")

if __name__ == "__main__":
  main()

sys.stdout.close()

###################################### END OF PROGRAM ######################################