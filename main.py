# Assignment #2


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
  fileName = "source1.txt"
  # input("Please specify the name of the source file: ")
  fileOutput = "output"
  # input("Please specify a name for the output file: ")

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
                lexemes = lexer.lexer(tokens)

                Syntax = syntax.syntaxAnalyzer(lexemes)

                if not Syntax: 
                  return "Syntax Error"
                
        return  
  print("Invalid source file.")

if __name__ == "__main__":
  main()

sys.stdout.close()

###################################### END OF PROGRAM ######################################