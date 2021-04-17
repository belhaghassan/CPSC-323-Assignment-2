
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

# Table created Using Hashtable with key: value pairs
E = {'id': {'T',"E'"}, '(': {'T',"E'"}}
Ep = {'+': {'+','T',"E'"}, '-': {'-','T',"E'"}, ')': "EPS", '$': "EPS"}
T = {'id': {'F',"T'"}, '(': {'-','T',"E'"}}
Tp = {'+': "EPS", '-': "EPS", '*': {'*','F',"T'"}, '/': {'/','F','T'},')': "EPS", '$': "EPS"} 
F = {'id': 'I', '(': {'(','E',')'}}
I = {'id': 'I'}

def syntaxAnalyzer(listoftokens)
  


# <Statement> -> <Declarative>
# <Declarative> -> <Type> <ID>
#  <Type> -> bool | float | int


































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

