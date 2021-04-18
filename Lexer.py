# Define keywords / separators / operators
SEPARATORS = ["(", ")", "{", "}", "[", "]", ",", ".", ":", ";"]
OPERATORS = ["*", "+", "-", "=", "/", ">", "<", "%", "==", "<=", ">=", "++", "--", "!="]
KEYWORDS = [
    "int", "float", "bool", "True", "False", "if", "else", "then", "endif",
    "endelse", "while", "whileend", "do", "enddo", "for", "endfor", "STDinput",
    "STDoutput", "and", "or", "not"
]

def FSM(token):  
  # d = {0 - 9}
  # a = {a-z, A-Z}

  # Sigma - {a,d,.,_,$}
  # Q = {0,1,2,3,4}
  # q(0) - state 1
  # F - {2,3,4}
  
  # N - stateTable
  stateTable = [[0, "a", "d", ".", "_", "$"],
                [1,   2,   3,   0,   0,   0],        # 1st Character
                [2,   2,   2,   0,   2,   2],        # IDENTIFIERS (ACCEPTING STATE)
                [3,   0,   3,   4,   0,   0],        # INTEGERS (ACCEPTING STATE)
                [4,   0,   4,   0,   0,   0]]        # REAL NUMBERS (ACCEPTING STATE)

  currentState = 1

  for i in token:
    if currentState == 1:                            ## 1ST CHARACTER
      if i.isdigit():
        currentState = stateTable[1][2]              #3
      elif i.isalpha():
        currentState = stateTable[1][1]              #2
      else:
        currentState = stateTable[1][5]              #0
    elif currentState == 2:                          ## identifier
      if not i.isdigit() and not i.isalpha() and not i == '_' and not i == '$':
        currentState = stateTable[2][3]              #0
    elif currentState == 3:                          ## integer
      if not i.isdigit() and not i == '.':
        currentState = 0
      elif i == ".":
        currentState = stateTable[3][3]              #4; otherwise remain the same
    elif currentState == 4:  
      if not i.isdigit(): 
        currentState = 0
  return currentState

#Lexer function takes in a list of strings to analyze 
def lexer(listoftokens): 
  lexList = []
  # Traverses each token in the list of tokens to see if they match any  
  # any that are initialized in the lists - KEYWORDS, OPERATORS, SEPARATORS. 
  # Otherwise the token will be passed through a Finite State Machine to
  # identify and validate it. 
  for token in listoftokens:
    if token in OPERATORS: 
      print("Token: OPERATOR\t\t\t\t\tLexeme:", token)
    elif token in SEPARATORS: 
      print("Token: SEPARATOR\t\t\t\tLexeme:", token)
    elif token in KEYWORDS:
      print("Token: KEYWORD\t\t\t\t\tLexeme:", token)
    else: 
      state = FSM(token)
      if state == 2:                       # State 2 = IDENTIFIERS (ACCEPTING STATE)
        print("Token: IDENTIFER\t\t\t\tLexeme:", token)
        token = "id"
      elif state == 3:                     # State 3 = INTEGERS (ACCEPTING STATE)
        print("Token: INTEGER\t\t\t\t\tLexeme:", token)
      elif state == 4:                     # State 4 = REAL NUMBERS (ACCEPTING STATE)
        print("Token: REAL\t\t\t\t\t\tLexeme:", token)
      else:
        print("Token: INVALID\t\t\t\t\tLexeme:", token)
    lexList.append(token)
  return lexList