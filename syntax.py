from collections import deque
############# COMMENTS #########################################################
# GRAMMAR/SYNTAX - PRODUCTION RULES (FROM LECTURES)
# Arithmetic expressions rules:
#    <Expression> -> <Expression> + <Term> | <Expression> - <Term> | <Term>
#    <Term> -> <Term> * <Factor> | <Term> / <Factor> | <Factor>
#    <Factor> -> ( <Expression> ) | <ID> | <Num>
#    <ID> -> id
#     *the <Num> rule is OPTIONAL 

#    E -> <E> + <T> | <E> - <T> | <T>
#    T -> <T> * <F> | <T> / <F> | <F>
#    F -> ( <E> ) | <I> 
#    I -> id

#   G = {T,N,S,R}
#        T = {+,-,*,/,(,),id}
#        N = {E,T,F,I} 
#        S = E
#        R = {
#            1. E  --> E + T             |   E  --> TE'
#            2. E  --> E - T | T         |   E' --> +TE' | -TE' | EPS
#            4. T  --> T * F | T / F     |   T  --> FT' 
#            6. T  --> F                 |   T' --> *FT' | /FT' | EPS
#            7. F  --> ( E ) | I         |   F  --> ( E ) | I  
#            9. I  --> id                |   I  --> id
#            }

#       First(E)  = {(,id}              Follow(E)   = {$,)}
#       First(E') = {+, -, EPS}         Follow(E')  = {$,)}
#       First(T)  = {(,id}              Follow(T)   = {+,-,$,)}
#       First(T') = {*,/,EPS}           Follow(T')  = {+,-,$,)}
#       First(F)  = {(,id}              Follow(F)   = {*,/,+,-,$,)}
#       First(I)  = {id}                Follow(I)   = {*,/,+,-,$,)}

        
#       id     +      -     *      /     (     )     $
# E  |  TE' |      |      |      |     | TE' |     |     |
#    -----------------------------------------------------
# E' |      | +TE' | -TE' |      |     |     | EPS | EPS |
#    -----------------------------------------------------
# T  |  FT' |      |      |      |     | FT' |     |     |
#    -----------------------------------------------------
# T' |      | EPS  | EPS  | *FT' | /FT'|     | EPS | EPS |
#    -----------------------------------------------------
# F  |   I  |      |      |      |     | (E) |     |     |
#    -----------------------------------------------------
# I  |  id  |      |      |      |     |     |     |     |
#    -----------------------------------------------------

Rules = {
    0: "E  --> TE'", 
    1: "E' --> +TE'", 
    2: "E' --> -TE'", 
    3: "E' --> EPS",
    4: "T  --> FT'", 
    5: "T' --> *FT'", 
    6: "T' --> /FT'", 
    7: "T' --> EPS",
    8: "F  --> (E)", 
    9: "F --> I", 
    10: "I  --> id" 
}

def symbolIndex(lexemes,nTerminals): 
  
  stackSwitcher = {"E": 0,"E'": 1,"T": 2,"T'": 3,"F": 4,"I": 5}
  lexSwitcher = {"id": 0,"+": 1,"-":2,"*": 3,"/": 4,"(": 5,")": 6,"$": 7}

  # Returns index of passed arguments in table
  return stackSwitcher.get(Lexemes), lexSwitcher.get(nTerminals)



rulesTable = [
  [   "TOS"  ,   'id'   ,      '+'     ,     '-'      ,    '*'       ,      '/'    ,     '('     ,  ')',  '$' ],
  [    "E"   ,['T',"E'"],    None      ,    None      ,    None      ,     None    , ['T',"E'"]  , None, None ],
  [    "E'"  ,   None   ,['+','T',"E'"],['-','T',"E'"],    None      ,     None    ,    None     ,"EPS","EPS" ],
  [    "T"   ,['F',"T'"],    None      ,    None      ,    None      ,     None    , ['F',"T'"]  , None, None ],
  [    "T'"  ,   None   ,     "EPS"    ,    "EPS"     ,['*','F',"T'"],['/','F','T'],    None     ,"EPS", "EPS"],
  [    "F"   ,   'I'    ,     None     ,    None      ,    None      ,     None    ,['(','E',')'], None, None ],
  [    "I"   ,   "id"   ,     None     ,    None      ,    None      ,     None    ,    None     , None, None ] 
]

def syntaxAnalyzer(listoftokens):
  
  Lexemes = listoftokens
  Lexemes.append("$")

  Stack = deque("$")
  Stack.append('E')
  lexIndex = 0

  ####### TEST - checking contents ###########################################
  print("\nChecking contents of rulesTable: ")
  
  for item in rulesTable:
    print(item)
  
  print("\nChecking contents of Stack[-1]:")
  print(Stack[-1])

  print("\nChecking contents of Lexemes: ")
  print(Lexemes[lexIndex])

  t = Stack[-1]
  i = Lexemes[lexIndex]
  print("\nChecking contents of rulesTable at [t, i]: ")
  #print(rulesTable[t,i])
  print(rulesTable[0], [1])

  test = "id"

  if test == (rulesTable[0][1]): #[0][1] == 'id'; [0][2] == '+'; etc)
    print("match")
  else:
    pass

  for item in rulesTable[0]:
    print(item)
  ############################################################################

  while not Stack:
    t = Stack[-1]
    i = Lexemes[lexIndex]
    if t in listoftokens: 
      if t == i:  
        pop(t)
        lexIndex += 1
      else: "Error"
    else:
      t_index, i_index = symbolIndex(t,i)
      print("\nprint table values")
      print(rulesTable[t_index, i_index])
      if not rulesTable[t_index, i_index]:       # needs to be if not None but only works without "not"
        Stack.pop()
        tableVal = rulesTable[t_index, i_index]   # Need to make t and i indexes that match table 
        print("\nprint table values")
        print(rulesTable[t_index, i_index])
        tableVal.reverse()
        print("\nprint table values in reverse")
        print(tableVal)
        for i in tableVal:
          Stack.append(i)       # Only way Stack changes from intial 'E'
      else:
        return "Error"
  return 



# <Statement> -> <Declarative>
# <Declarative> -> <Type> <ID>
#  <Type> -> bool | float | int






























# Table created Using Hashtable with key: value pairs
# E = {'id': {'T',"E'"}, '(': {'T',"E'"}}
# Ep = {'+': {'+','T',"E'"}, '-': {'-','T',"E'"}, ')': "EPS", '$': "EPS"}
# T = {'id': {'F',"T'"}, '(': {'-','T',"E'"}}
# Tp = {'+': "EPS", '-': "EPS", '*': {'*','F',"T'"}, '/': {'/','F','T'},')': "EPS", '$': "EPS"} 
# F = {'id': 'I', '(': {'(','E',')'}}
# I = {'id': 'I'}



# *using a semicolon ; at the end of the rule is OPTIONAL 

#       ADDITION / SUBTRACTION
#       E  --> TE'
#       E' --> +TE' | -TE' | EPS
#
#       MULTIPLICATION / DIVISION
#       E  --> TE'
#       E' --> *TE' | /TE' | EPS
#
#       "(" AND ")"
#       F  --> ( E )

# max + min

# queue = ksjdflkjdlkljfkjf


# Function E
# def E(token):
#   E = False
#   if T:
#     if Q:
#       print(' E --> TQ')
#       E = True
#   return E

# # Function Q
# def Q(token):
#   Q = False
#   cc = token
#   if cc == '+' or cc == '-':
#     if T:
#       if Q:
#         print (' Q --> ' + cc + 'TQ')
#         Q = True
#   else:
#     if cc in [')', '$']:
#       backup()
#       print (' Q --> eps')
#       Q = True
#   return Q

# # Function T
# def T(token):
#   T = False
#   if F:
#     if R:
#       print (' T --> FR')
#       T = True
#   return T

# # Function R
# def R(token):
#   R = False
#   cc = token
#   if cc == '*' or cc == '/':
#     if F:
#       if R:
#         print (' R --> ' + cc + 'FR')
#         R = True
#   else:
#     if cc in ['+','-',')','$']:
#       print (' R --> eps')
#       backup()
#       R = True
#   return R

# # Function F
# def F(token):
#   F = False
#   cc = token
#   if cc in ['a-zA-Z']:
#     print (' F --> id')
#     F = True
#     # test without this 2nd if clause
#   elif cc == '(':
#     if E:
#       cc = token
#       if cc == ')':
#         print (' F --> (E)')
#         F = True
#   else:
#     pass
#   return F

# def backup():
#   pass

