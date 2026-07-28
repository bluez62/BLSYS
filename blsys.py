#Python

level = 0
levelreq = 0
blsys = {}

def var(var_name, var_value, storage_dict):
    blsys[var_name] = var_value

def InputVar(var_name, text, bType, blsys):
    if bType == int:
        blsys[var_name] = int(input(text))
    if bType == str:
        blsys[var_name] = str(input(text))

def DisplayMessage(x):
    if level == levelreq:
        print(x)

def exit_block():
    global level, levelreq
    levelreq -= 1
    if level > levelreq:
        level -= 1

def blsysIf(var_name, operator, value, actions):
    global levelreq, level
    levelreq += 1
    
    def check_condition():
        current_val = blsys[var_name]
        if operator == "<=": return current_val <= value
        if operator == "==": return current_val == value
        if operator == ">=": return current_val >= value
        if operator == ">":  return current_val > value
        if operator == "<":  return current_val < value
        return False

    if check_condition():
        if level == (levelreq - 1):
            level += 1
            for action in actions:
                action()
            level -= 1
            
    exit_block()

def blsysWhile(var_name, operator, value, actions):
    global levelreq, level
    levelreq += 1
    
    def check_condition():
        current_val = blsys[var_name]
        if operator == "<=": return current_val <= value
        if operator == "==": return current_val == value
        if operator == ">=": return current_val >= value
        if operator == ">":  return current_val > value
        if operator == "<":  return current_val < value
        return False

    while check_condition():
        if level == (levelreq - 1):
            level += 1
            for action in actions:
                action()
            level -= 1
            
    exit_block()

def wait(time):
    pass




#BLSYS

def plusCalc(): DisplayMessage(blsys["firstNumber"] + blsys["secondNumber"])
def minusCalc(): DisplayMessage(blsys["firstNumber"] - blsys["secondNumber"])
def multCalc(): DisplayMessage(blsys["firstNumber"] * blsys["secondNumber"])
def divideCalc(): DisplayMessage(blsys["firstNumber"] / blsys["secondNumber"])

InputVar("firstNumber", "First Number: ", int, blsys)
InputVar("operator", "+, -, X, or /: ", str, blsys)
InputVar("secondNumber", "Second Number: ", int, blsys)

blsysIf("operator", "==", "+", [plusCalc])
blsysIf("operator", "==", "-", [minusCalc])
blsysIf("operator", "==", "X", [multCalc])
blsysIf("operator", "==", "/", [divideCalc])



