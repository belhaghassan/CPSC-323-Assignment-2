# Assignment #2

import pandas as pd
from collections import deque
import Lexer as lexer
import functions as func
import os
import sys
from syntax_analysis_helper import syntaxError, convertRule, printProductionRules

# LL Table Parser Definitions
tbl_predict_parser = pd.read_csv("tbl-parser.csv", delimiter=",", encoding="utf-8-sig")
tbl_predict_parser.set_index("TOS", inplace=True)
term_list = tbl_predict_parser.columns.values

# Define Stacks
Stack = deque()
Lexemes = deque()

def main():
  #Prompts user for source file and output file
  fileName = "source2.txt" 
  # input("Please specify the name of the source file: ")
  #fileName = "source1.txt"
  fileOutput = "outputtest2"
  # input("Please specify a name for the output file: ")
  #fileOutput = "output"

  code = ""
  syntaxCorrect = True

  #Check to see if file exists
  if os.path.exists(fileName):
    sys.stdout = open(fileOutput,"w")

    with open(fileName) as source:
        for row in source:
            if (not row.strip()):
                pass
            elif ((row.lstrip())[0] == '!'):
                pass
            else:
                code += row
        
        # Push $ onto the stack
        Stack.append("$")

        #Push $ at the end of input string
        code = code + " $"

        #Push starting symbol on the stack
        Stack.append("S")

        #Separate each of the elements with white space in case they're packed together
        #NOTE: if the source code is "a+b", the variable code contains ("a","+","b","$").  The "$" is from line 49
        lineOfCode = func.separateElements(code)

        #Split up the each element
        tokens = lineOfCode.split()

        #Pass each token to the lexer.  Check if it's an operator, separator, keyword.  If so, append to temp stack as is
        #Otherwise, if token is evaluated as INT, REAL, etc.  Append that to the stack.
        #For example, ("a","+","b","$") will stored as ("ID","+","ID","END")
        for token in tokens:
            lexList = lexer.lexer(token)

            if (lexList == "OPERATOR" or lexList == "SEPARATOR" or lexList == "KEYWORD"):
                Lexemes.append(token)
            else:
                Lexemes.append(lexList)

        ## Checking what was appended 
        for item in Lexemes:
              print(item)


        #While stack not empty do
        while (len(Stack) > 0):
          #Debug Station:
          debugList = ["", "", ""]
          debugList[0] = "".join(Stack)
          debugList[1] = "".join(Lexemes)

          #let terminal = TOS symbol and i=incoming token
          terminal = Stack[-1] #Peek last element in deque or top of stack
          incomingToken = Lexemes[0] #Peek first element in deque or front of queue
       
          print("Token: " + incomingToken + "\n")


        ###################################TESTING########################################
          #Testing - checking contents of Lexemes
          print("The Lexemes contains: ")
          for item in Lexemes:
              print(item)
          #Testing - checking contents of Stack
          print("The Stack contains: ")
          for item in Lexemes:
              print(item)
          ##################################TESTING########################################


          if any(item == terminal for item in term_list):
              if (terminal == incomingToken):
                    debugList[2] += "pop(" + Stack.pop() + ")"
                    debugList[2] += ", lexur() popped " + Lexemes.popleft()
              else:
                     syntaxCorrect = False
                     print("  Recieved: " + Lexemes.popleft() +
                                     "  Expected: " + Stack.pop() + "\n")
                     break
          else:
                 #if Table[t,i] has entry then
              if (str(tbl_predict_parser.loc[terminal, incomingToken]) != "nan"):
                     poppedValue = Stack.pop()
                     debugList[2] += "pop(" + poppedValue + ")"  #Output to debug
                     pushValues = list() #push Table[t,i] in reverse order
                     lookUp = tbl_predict_parser.loc[terminal, incomingToken]
                     pushValues = lookUp.split() #Split look up value by whitespace
                     #print(printProductionRules(poppedValue, pushValues) + "\n") #Print Production Rules
                     pushValues.reverse() #Reverse order of list of TOS
                     debugList[2] += ", push(" #Output to debug
                     for values in pushValues:
                         debugList[2] += values
                         #If Eplison, do not append into values
                         if (str(tbl_predict_parser.loc[terminal, incomingToken]) != "ε"):
                            Stack.append(values)
                            debugList[2] += ")"  #Output to debug
              else:
                     syntaxCorrect = False
                     print("Syntactically incorrect" + "\n")
                     break   #Do not continue to compile

        # #Clear items in Lex
        Lexemes.clear()

        #If syntax is correct
        if(syntaxCorrect == True):
            print("Finished")
        return

  print("Invalid source file.")

if __name__ == "__main__":
  main()

sys.stdout.close()