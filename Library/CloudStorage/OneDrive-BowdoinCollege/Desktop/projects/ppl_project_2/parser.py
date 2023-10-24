#CSCI 2320: RD and more specifically LL(1) parser
#Lexe Le
#Grammar productions
#Expr -> Term {(+|-) Term}
#Term -> Factor {(+|-) Factor}
#Factor -> intLiteral

import sys

#TODO: Should I add a failure case?
#      
tokens = ["intLiteral", "+", "intLiteral", "*", "intLiteral"] #input
token_pointer = 0

def main():
    expression() #start symbol
    if token_pointer < len(tokens): #could not consume the whole input
        error("Incomplete expression. Error at index " + str(token_pointer))
    else:
        print("Valid Expression!")

def lookup(t):
    return token_pointer < len(tokens) and tokens[token_pointer] == t

def consume():
    token_pointer += 1

def program():
    global token_pointer

    if lookup("type"):
        consume()
    if lookup("main"):
        consume()
    if lookup("("):
        consume()
    if lookup(")"):
        consume()
    if lookup("{"):
        consume()

    declarations() # don't consume AFTER calling
    statements()

    if lookup("}"):
        consume()
    
def declarations():
    global token_pointer
    while token_pointer < len(tokens):
        declaration()
        consume()

#look at first symbol nonterminal 
def declaration():
    global token_pointer
    

    if lookup("id"):
        consume()
    else:
        sys.exit("Failure")

    while token_pointer < len(tokens) and lookup(","):
        consume()  

    if lookup(";"):
        consume()
    else:
        sys.exit("Failure")


def statements():
    global token_pointer
    while token_pointer < len(tokens) and \
        lookup("{") or lookup("id") or lookup("print") \
        or lookup("if") or lookup("while") or lookup("return"):
        statement()
        

def statement():
    global token_pointer
    while token_pointer < len(tokens) and \
        lookup("{") or lookup("id") or lookup("print") \
        or lookup("if") or lookup("while") or lookup("return"): 
        #how do we best determine when to get out of the loop
        if lookup("{"):
            block()
        if lookup("id"):
            assignment()
        if lookup("print"):
            printStmt()
        if lookup("if"):
            ifStatement()
        if lookup("while"):
            whileStmt()
        if lookup("return"):
            returnStmt()


def block():
    global token_pointer
    if lookup("{"): #this might be redundant 
        consume()
    statements()
    if lookup("}"):
        consume()


def assignment():
    global token_pointer
    if lookup("id"): #this might be redundant 
        consume()
    if lookup("equOp"):
        consume()
    expression() 

def printStmt(): 
    global token_pointer
    if lookup("print"): #is this redundant? checking already in the statement function.
        consume()
        expression()
        if lookup(";"):
            consume() #add a failure case incase it doesn't work?


def ifStatement():
    global token_pointer
    if lookup("if"): #this might be redundant 
        consume()
        if lookup("("):
            consume()
            expression()
            if lookup(")"):
                consume()
                statement()
                 # [ ] -> take it or leave it !!! figure out how to implement 
                if lookup("else"):
                    consume()
                    statement()
                    

def whileStmt():
    global token_pointer
    if lookup("("):
        consume()
        expression()
        if lookup(")"):
            consume()
            statement()
    else:
        sys.exit("Failure")


def returnStmt():
    global token_pointer
        expression()
        if lookup(";"):
            consume()
        else:
            sys.exit("Failure")

def assignOp():
    global token_pointer
    if lookup("equOp"):
        consume()

def expression():
    global token_pointer
    conjuction()
    while token_pointer < len(tokens):
        if lookup("||")
            consume()
            conjunction()

def conjection
    global


        

        
    # conjunction() or while token_pointer < len(tokens):
    #     conjunction()

# #Expr -> Term {(+|-) Term}
# # brace = while loop because 0 or more times
# def expr():
#     global token_pointer
#     term()
#     while token_pointer < len(tokens) and (tokens[token_pointer]=="+" or tokens[token_pointer]=="-"):
#         token_pointer += 1
#         term()

#Term -> Factor {(+|-) Factor}
def term():
    global token_pointer
    factor()
    while token_pointer < len(tokens) and (tokens[token_pointer] == "*" or tokens[token_pointer] == "/"):
        token_pointer += 1
        factor()

#Factor -> intLiteral
def factor():
    global token_pointer
    if token_pointer < len(tokens) and tokens[token_pointer] == "intLiteral":
        token_pointer += 1
    else: #operand (intLiteral) missing
        error("Missing intLiteral at index " + str(token_pointer))
    
def error(msg):
    print(msg)
    exit()

if __name__ == "__main__":
    main()
