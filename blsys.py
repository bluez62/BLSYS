#Python
import time

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

def wait(amount):
    time.sleep(amount)

def ToInt(var_name):
    blsys[var_name] = int(blsys[var_name])

def ToStr(var_name):
    blsys[var_name] = str(blsys[var_name])

def ToFlt(var_name):
    blsys[var_name] = float(blsys[var_name])

def ToBool(var_name):
    blsys[var_name] = bool(blsys[var_name])

#BLSYS
def plusCalc(): DisplayMessage(blsys["first_number"] + blsys["second_number"])
def minusCalc(): DisplayMessage(blsys["first_number"] - blsys["second_number"])
def multiplyCalc(): DisplayMessage(blsys["first_number"] * blsys["second_number"])
def divideCalc(): DisplayMessage(blsys["first_number"] / blsys["second_number"])

def beginCalculator():
    InputVar("first_number", "First Number: ", int, blsys)
    InputVar("operator", "Operator: ", str, blsys)
    InputVar("second_number", "Second Number: ", int, blsys)
    blsysIf("operator", "==", "+", [plusCalc])
    blsysIf("operator", "==", "-", [minusCalc])
    blsysIf("operator", "==", "*", [multiplyCalc])
    blsysIf("operator", "==", "/", [divideCalc])

var("1", 1, blsys)
blsysWhile("1", "==", 1, [beginCalculator])
