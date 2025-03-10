# Copyright (c) 2025 Thomas Duggan
# This work is licensed under CC BY-SA 4.0


# Global variables:
registers = []	# amount of locations where variables can be stored
line = -1		# current code line


def init(register_count):
    """Set up the simulated CPU for use.

    This function should set `registers` to be a list with
    `register_count` values, each of which should be set to 0.
    It should also set the program counter to 0.

    Parameters
    ----------
    register_count : int
        How many registers this CPU should have.
        This should be a positive integer; if it is not,
        the function returns False.

    Returns
    -------
    bool : True if register_count was a valid integer
    """
    global registers
    global line
    stop = False
    
    ############### Failsafes ###############
    
    if (type(register_count) == str) or (type(register_count) == bool):
        initialized = False
        stop = True
        
    ############### Register Initialization ###############
        
    if stop == False:
        register_count = int(register_count)
        
    if (stop == False) and (register_count < 1):
        initialized = False
        
    if (stop == False) and (register_count >= 1):
        registers = []
        initialized = True
        for uwu in range(register_count):
            registers += [0]
        line = 0  
        
    return initialized


def program_counter():
    """What is the current program counter?

    Returns
    -------
    an integer representing the next instruction to be executed
    """
    global line
    return line


def register_values():
    """What are the current register values?

    Returns
    -------
    a list of register values
    """
    global registers
    return registers


def run_instruction(instruction):
    """Run a single instruction on the simulated CPU.

    Parameters
    ----------
    instruction : str
        A single instruction for the simulated CPU to excute.

    Returns
    -------
    bool : whether or not the instruction was valid
    """
    global registers	# < Imports global vars at top of script
    global line			# < ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    stop = False		# Used for Failsafes
    success = False		# Assumes invalid instruction
    
    
    ############### Failsafes ###############
    
    backup = tuple(registers)
    # Used to revert registries (see end of module for more)
    
    if type(instruction) != str:
        success = False
        stop = True
    # Determines if input is a string or not
    

    if "set" in instruction or "Set" in instruction:
        if "to" not in instruction:
            stop = True
        if "to r" in instruction:
            stop = True
            
    if "multiply" in instruction or "Multiply" in instruction or "divide" in instruction or "Divide" in instruction:
        if "by r" not in instruction:
            stop = True
            
    if "if" in instruction or "If" in instruction:
        if "goto" not in instruction:
            stop = True
            
    if "subtract" in instruction or "Subtract" in instruction:
        if "from r" not in instruction:
            stop = True
            
    if "add" in instruction or "Add" in instruction:
        if "to r" not in instruction:
            stop = True
            
    if instruction == "halt" or instruction == "Halt":
        stop = True
        success = True
    
    # Determines if instruction was formatted correctly
    
    
    ########## Registry Number Redefinition ##########
    
    if stop == False:    

        temp_list = []
        num_loc = []
        for i in range(len(instruction)):
            
            if i != 0:
                if (((instruction[i] != '0') and (instruction[i] != '1') and (instruction[i] != '2') and (instruction[i] != '3') and (instruction[i] != '4') and (instruction[i] != '5') and (instruction[i] != '6') and (instruction[i] != '7') and (instruction[i] != '8') and (instruction[i] != '9')))		and		((instruction[i-1] == '0') or (instruction[i-1] == '1') or (instruction[i-1] == '2') or (instruction[i-1] == '3') or (instruction[i-1] == '4') or (instruction[i-1] == '5') or (instruction[i-1] == '6') or (instruction[i-1] == '7') or (instruction[i-1] == '8') or (instruction[i-1] == '9')):
                    temp_list += ["BREAK"]
                    num_loc += ["break"]
            # If previous character is not a number, and current character is, add "BREAK" to seperate numbers
            # This should not happen on first character (chr 0)
                    
            if instruction[i] == '0' or instruction[i] == '1' or instruction[i] == '2' or instruction[i] == '3' or instruction[i] == '4' or instruction[i] == '5' or instruction[i] == '6' or instruction[i] == '7' or instruction[i] == '8' or instruction[i] == '9':
                temp_list += [int(instruction[int(i)])]
                num_loc += [i]
            # Adds current number to new list
            
        
        stop_2 = False
        for x in range(len(temp_list)):
            if temp_list[x] == "BREAK" and stop_2 == False:
                break_location = x
                stop_2 = True
            # Determines location of first "BREAK" in list
            
            
        rX = int(((str(temp_list[:(break_location ) ]))[1:-1])[::3])
        rY = int(((str(temp_list[(break_location+1):]))[1:-1])[::3])
            # Converts numbers in list to strings so it can be iterated through
            # Then converts the iterated string to an integer
        
        
        ########## Actual Instruction Execution ##########
        
        if instruction[0:5] == 'add r' or instruction[0:5] == 'Add r':
            registers[rY] += registers[rX]
            success = True
            line += 1
            # Checks which instruction was executed
            # Adds value in rY to value in rX
            
            
        if instruction[0:10] == 'subtract r' or instruction[0:10] == 'Subtract r':
            registers[rY] -= registers[rX]
            success = True
            line += 1
            # Checks which instruction was executed
            # Subtracts value in rY to value in rX
            
            
        if instruction[0:10] == 'multiply r' or instruction[0:10] == 'Multiply r':
            registers[rX] *= registers[rY]
            success = True
            line += 1
            # Checks which instruction was executed
            # Muliplys value in rX to value in rY
           
        if instruction[0:8] == 'divide r' or instruction[0:8] == 'Divide r':
            if registers[rY] != 0:
                registers[rX] /= registers[rY]
                success = True
                line += 1
            if registers[rY] == 0:
                success = False
            # Checks which instruction was executed
            # Divides value in rX to value in rY
            # Prevents division by zero
            
        if instruction[0:5] == 'set r' or instruction[0:5] == 'Set r':
            if rX > (len(registers)-1): # fails if attempting to assign a value outside of range
                success = False
            else:
                registers[rX] = rY
                success = True
                line += 1
            # Checks which instruction was executed
            # Sets value in rX to value given

            
        if instruction[0:4] == 'if r' or instruction[0:4] == 'If r':
            if registers[rX] != 0:
                line = rY
                success = True
            # Checks which instruction was executed
            # If the value in rX is NOT zero, the line will be changed to the line requested
            
        if line < 1 and registers != []:
            line = 0
            # Resets line back to zero if it ever becomes less than 1
            # Only happens if init() has happened
            
        if instruction[num_loc[0]-1] != "r":
            registers = list(backup)
            success = False
            # resets register values at end 
            
            
    return success


def run_program(program):
    """Run a program consisting of a list of instructions.

    Parameters
    ----------
    program : list[str]
        A list of instruction strings. The CPU will start by executing instruction
        0 and continue until it reaches a `halt` instruction.

        If the list of instructions is empty, this function returns False.

        If the program goes past the end of the program without executing a
        `halt` instruction, this function returns False.

    Returns
    -------
    bool : whether or not the program executed each instruction successfully
    """
    global line
    global registers
    success = False
    halt_hit = False
    line = 0
    stop = False
    
    for x in range(len(program)):
        if type(program[x]) != str:
            success = False
            stop = True
    
    while stop == False:
        
            
        if halt_hit == True:
            break
            
        if line >= len(program):
            break
            
        if str(program[line]) == "halt" or str(program[line]) == "Halt":
            success = True
            halt_hit = True
                
        else:
            
            if (run_instruction(program[line])) == False:
                break
            if line >= len(program):
                break
            else:
                run_instruction(program[line])
                
    return success
    