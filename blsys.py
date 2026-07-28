level = 0
levelreq = 0
blsys = {}

def var(var_name, var_value, storage_dict):
    storage_dict[var_name] = var_value

def DisplayMessage(x):
    if level == levelreq:
        print(x)

def exit_block():
    global level, levelreq
    levelreq -= 1
    if level > levelreq:
        level -= 1

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



#INSTRUCTIONS for BLSYS

#Step 1: Defining Variables
#Variables are basically just things that hold a value, this value can be a number, some text, or even a
#boolean (A boolean is "true" or "false")

#Here's how we define a variable:
#var("x", 1, blsys)

#Let's break that down!
#var is short for var, the var command is always lowercase and also has brackets right after it.
#In the brackets, put the name of your variable in quotation marks, then we put a comma after the
#quotation marks. Next you put what value you want that variable to hold.
#If we want that value to be a number, then you just put the number, But if you want it to be
#text, then you need to put it in quotation marks, here's an example:


#Number:
#var("x", 1, blsys)

#Text:
#var("x", "Hello!", blsys)


#Then, we put a comma after the value, and then you write blsys. (The blsys part never changes, you always
#put blsys there.) A good way to remember blsys is because bl is short for Bluez, and sys is short for system.


#Step 2: Displaying Messages
#To display a message, we need to use the command DisplayMessage. Here is a quick example:

#DisplayMessage("Hi!")

#You just write DisplayMessage, then you put brackets, and then, like last time, if its a number, just write it.
#But if its text, then put it in quotation marks. But there is also a way to display a variable, here is an
#example:

#var("exampleVariable", 395, blsys)
#DisplayMessage(blsys["exampleVariable"])

#(this example would display 395.)



#There are a few changes when tryinig to display a variable, you write blsys and then put square brackets, and
#then you put the variable name in quotation marks.

#Step 3: If & While Statements:
#Let's say you only wanted to trigger some code if a certain condition was met. That is possible in blsys!
#Here's a quick example:

#var("x", 5, blsys)
#def step1(): DisplayMessage(blsys["x"])
#blsysIf("x", "==", 5, [step1])

#Let's break that down!
#The first line is defining a varriable called x and setting it to 5.
#The second line is defining a function called step1 and setting it to display the variable x.
#And the third line says if x = 5, then trigger step1.

#Functions are basically just code stored together and named. If you want to trigger code with an if statement,
#then the code HAS to be in a function. You can even make multiple step functions, like step1, step2, step 3, etc.
#And then you could trigger all of those functions on a condition like this:

#blsysIf("x", "==", 5, [step1, step2, step3])

#If statements work like this: First, you put blsysIf, and then put brackets.
#Then, at the start of the brackets, put the variable name in quotes. Put a comma afterwards and then you put
#more quotes, These 2nd quotes are the operator, so == basically just means =, > is greater than, >= is greater
#than or equal, and so on. Then you put another comma, and put the number it is compared against.
#You can also put blsys["variableName"] in the number part to compare your variable against another variable.
#Then, put one more comma, and then put square brackets, and put all your step functions in it.

#While statements work almost the exact same as if statements, except they don't just trigger once, they
#keep looping. The only difference is that you put blsysWhile instead of blsysIf.

#Step 4: Additional Information:
#Let's go back to step 1, you can do var("x", 5, blsys), but then you could do something like this:

#var("y", blsys[x]+7, blsys)

#And that would define a variable called y and set it to x+7, so 12.


#And now lastly, here is some example code for you to refer to:

#var("x", 5, blsys)
#var("z", 11, blsys)

#def step1(): var("z", blsys["z"] + blsys["x"], blsys) 

#def step2(): DisplayMessage(f"Z Value: {blsys['z']}")

#blsysWhile("z", ">=", 10, [step1, step2])

#That example code will keep adding z and y together, and displaying the result, until the result gets past
#999999999999.

#Also, don't actually put a # before every line of code, that is just used to put a comment so that none of these
#instructions register as code. And you can also put empty lines between lines to categorize your code into
#sections, but that's not required.






var("countdown", 10, blsys)

def decrement(): var("countdown", blsys["countdown"] - 1, blsys)
def show_num(): DisplayMessage(blsys["countdown"])
def blast_off(): DisplayMessage("Blast off!")

blsysWhile("countdown", ">=", 1, [show_num, decrement])
blsysIf("countdown", "==", 0, [blast_off])

