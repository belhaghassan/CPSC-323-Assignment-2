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

Rules {0: "E  --> TE'", 1: "E' --> +TE'", 2: "E' --> -TE'", 3: "E' --> EPS",
        4: "T  --> FT'", 5: "T' --> *FT'", 6: "T' --> /FT'", 7: "T' --> EPS",
        8: "F  --> ( E )", 9: "F --> I", 10: "I  --> id" }
}
T_ID = 0
T_PLUS = 1
T_MINUS = 2
T_MUL = 3
T_DIV = 4
T_LPAR = 5
T_RPAR = 6
T_END = 7

rulesTable = [
  [['T',"E'"],    None      ,    None      ,    None      ,     None    ,  ['T',"E'"] , None, None ],
  [   None   ,['+','T',"E'"],['-','T',"E'"],    None      ,     None    ,    None     ,"EPS","EPS" ],
  [['F',"T'"],    None      ,    None      ,    None      ,     None    , ['F',"T'"]  , None, None ],
  [   None   ,     "EPS"    ,    "EPS"     ,['*','F',"T'"],['/','F','T'],    None     ,"EPS", "EPS"],
  [   'I'    ,     None     ,    None      ,    None      ,     None    ,['(','E',')'], None, None ],
  [   "id"   ,     None     ,    None      ,    None      ,     None    ,    None     , None, None ] 
]

def syntaxAnalyzer(listoftokens):
  
  Lexemes = listoftokens
  Lexemes.append("$")
  Stack = deque("$")
  Stack.append('E')
  lexIndex = 0
  while not Stack:
    t = Stack[-1]
    i = Lemexe[lexIndex]
    if t in listoftokens: 
      if t == i:  
        pop(t)
        lexIndex += 1
      else: "Error"
    else:
      TOS = Stack[-1] 
      print(TOS)
      print(TOS)
      # if TOS in 
  return True


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

