
############# COMMENTS #################################################################################
# GRAMMAR/SYNTAX - PRODUCTION RULES (FROM LECTURES)
# Arithmetic expressions rules:
#    E= <Expression> -> <Expression> + <Term> | <Expression> - <Term> | <Term>
#    T= <Term> -> <Term> * <Factor> | <Term> / <Factor> | <Factor>
#    F= <Factor> -> ( <Expression> ) | <ID> | <Num>
#    I= <ID> -> id
#     *the <Num> rule is OPTIONAL 

#   G = {T,N,S,R}

#        T = {+,-,*,/,(,),id}
#        N = {E,T,F,I,N} 
#        S = E
#        R = {
            #  E  --> E + T                             |   E  --> TE'
            #  E  --> E - T                             |   E' --> + T E' | epsilon
            #  E  --> T                                 |   E' --> - T E' | epsilon
            #  T  --> T * F                             |   T  --> * F T' | epsilon
            #  T  --> T / F                             |   T' --> / F T'  
            #  T  --> F                                 |   T  --> F  
            #  F  --> ( E )                             |   F  --> ( E ) 
            #  F  --> I                                 |   F  --> I 
            #  N  --> 0 | 1 | 2 | 3 | 4                 |   N  --> 0 | 1 | 2 | 3 | 4
            #     | 5 | 6 | 7 | 8 | 9                   |           | 5 | 6 | 7 | 8 | 9 
#            }

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
def E(token):
  E = False
  if T:
    if Q:
      print(' E --> TQ')
      E = True
  return E

# Function Q
def Q(token):
  Q = False
  cc = token
  if cc == '+' or cc == '-':
    if T:
      if Q:
        print (' Q --> ' + cc + 'TQ')
        Q = True
  else:
    if cc in [')', '$']:
      backup()
      print (' Q --> eps')
      Q = True
  return Q

# Function T
def T(token):
  T = False
  if F:
    if R:
      print (' T --> FR')
      T = True
  return T

# Function R
def R(token):
  R = False
  cc = token
  if cc == '*' or cc == '/':
    if F:
      if R:
        print (' R --> ' + cc + 'FR')
        R = True
  else:
    if cc in ['+','-',')','$']:
      print (' R --> eps')
      backup()
      R = True
  return R

# Function F
def F(token):
  F = False
  cc = token
  if cc in ['a-zA-Z']:
    print (' F --> id')
    F = True
    # test without this 2nd if clause
  elif cc == '(':
    if E:
      cc = token
      if cc == ')':
        print (' F --> (E)')
        F = True
  else:
    pass
  return F

def backup():
  pass

