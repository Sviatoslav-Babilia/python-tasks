import string #import library for working with simbols
inp = input() 
#function for checking is symbol in password
def sym_sec(sym, sec):
    res = False
    # checking symbol presence in sequence
    for s in sym: 
        if s in sec:
            res = True
            return res
    return res

def symbols(text):

    passw = text.split(',')#divide text to the passwords
    lowlet = string.ascii_lowercase #all letters in lowercase
    uplet = string.ascii_uppercase  #all letters in uppercase
    symbols = '*#+@' #special symbols
    result = [] 
    for item in passw: #iterate list of passwords
        if " " not in item: #checking for no_spaces
            if len(item) > 3 and len(item) < 7: #Checking length password
                if sym_sec(item, lowlet): #checking lowercase letter presence
                    if sym_sec(item, uplet): #checking uppercase letter presence
                        if sym_sec(item, symbols): #checking special symbols presence
                            result.append(item)# join correct passwort to result list
    return ','.join(result)   

print (symbols(inp))

