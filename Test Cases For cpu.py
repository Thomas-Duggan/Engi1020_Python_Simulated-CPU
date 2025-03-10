from cpu import *









# Change number to change what test to preform  ######################################

test = 0


######################################################################################

# Btw, this may be useful to copy/paste: ✅

################################## TEST 0: Autograder Fixes ############################################

if test == 0:
    print(init(4))									# True  ✅
    #sets 4 registry slots (up to r3)
    
    print(run_instruction("set r4 to 4"))			# False ✅ ❗
                # False due to r4 being out of range
    
    print(register_values()) 						# [0, 0, 0, 0] ✅
    
    
    print(init(2))									# True ✅
    
    print(register_values()) 						# [0,0] ✅
    
    print(run_instruction("add r1 to r0"))			# True ✅
    
    print(program_counter()) 						# 1 ✅


    print(init(4))									# True  ✅
    # sets 4 registry slots (up to r3)
    
    print(register_values()) 						# [0, 0, 0, 0] ✅
    
    print(run_instruction("set r-1 to 1"))			# False ✅ ❗
                # False due to "r-1" not existing
                
    print(register_values()) 						# [0, 0, 0, 0] ✅

    print(init(1))
    
    print(register_values())
    
    print(run_program(["set r0 to 42"]))
          
    print(register_values())

################################## TEST 1: Instructions ############################################

# Uses init(), run_instruction(), register_values(), and program_counter()


if test == 1:
    
    print(init(1))									# True  ✅
    # sets 1 registry slot  (up to r0)
    
    print(register_values()) 						# [0] ✅

    
    print(init(5))									# True  ✅
    # sets registry slots to 5 instead of 1 (up to r4)
    
    print(register_values()) 						# [0, 0, 0, 0, 0] ✅


    print(init(0))									# False ✅ ❗
                # False due to 0 registers

    print(run_instruction("set 2 to 2"))			# False ✅ ❗
                # False due to missing r
                
    print(run_instruction("set r2 to r2"))			# False ✅ ❗
                # False due to extra r
            
    print(run_instruction("set r2 to 2"))			# True  ✅
    # sets r2 to value 2

    print(run_instruction("set r3 to 3"))			# True  ✅
    # sets r3 to value 3

    print(run_instruction("set r4 to 4"))			# True  ✅
    # sets r4 to value 4

    print(run_instruction("add r3 to r3"))			# True  ✅
    # adds 3 to 3 to get 6 in r3

    print(run_instruction("subtract r3 to r3"))		# False  ✅❗
                # False due to missing "from"

    print(run_instruction("subtract r3 from r3"))	# True  ✅
    # subtracts 6 from 6 to get 0 in r3

    print(run_instruction("if r3 goto 69"))			# False ✅❗
                # False since r3 is 0 

    print(run_instruction("if r4 goto 420"))		# True  ✅
    # sets line to 420 since r4 is 4

    print(run_instruction("multiply r3 by r3"))		# True  ✅
    # multiplies 0 by 0 to get 0 in r3, and adds a line

    print(run_instruction("multiply r2 to r2"))		# False ✅ ❗
                # False due to missing "by"

    print(run_instruction("mulitply r3 by r3"))		# False ✅ ❗
                # False due to mispelt "multiply"
            
    print(run_instruction("divide r3 by r3"))		# False ✅ ❗
                # False due to division by zero

    print(run_instruction("halt"))					# True  ✅
    # runs nothing, but is True regardless

    print(register_values()) 						# [0, 0, 2, 0, 4] ✅
    
    print(program_counter()) 						# 421   ✅
    
    
    
################### TEST 2: Extreme Values ######################

# Uses init(), run_instruction(), register_values(), and program_counter()

if test == 2:
    
    print(init(500))								# True  ✅
    # sets 500 registry slots (up to r499)
    
    print(run_instruction("set r100 to 1000000"))	# True  ✅
    # sets r100 to value 1 million
    
    print(run_instruction("set r10 to 500000"))		# True  ✅
    # sets r100 to value 500 thousand
    
    print(run_instruction("set r482 to 010010000110100100100000"))	# True  ✅
    # sets r482 to binary for "hi"
    
    print(run_instruction("divide r10 by r100"))	# True  ✅
    # divides 500 thousand by 1 million (0.5)
    
    print(run_instruction("if r10 goto 80"))		# True  ✅
    # r10 is not zero
    
    print(run_instruction("if r95 goto 100"))		# False ✅  ❗
                # False due to r95 being zero
    
    print(register_values()) # Massive list that I am NOT writing
    print(program_counter()) 						# 80 ✅
    
    
################### TEST 3: Run Program ######################

if test == 3:
    
    x = ["set r2 to 2","set r3 to 3","set r4 to 4","add r3 to r3","subtract r3 from r3","multiply r3 by r3","halt"]
    print(init(5)) 									# True  ✅
    
    print(run_program(x))							# True  ✅
    
    print(register_values()) 						# [0, 0, 2, 0, 4] ✅
    
    print(program_counter()) 						# 6 ✅
    
    x = ["set r2 to 2","set r3 to 3","set r4 to 4","add r3 to r3","subtract r3 from r3","multiply r3 by r3"]
    print(init(5))									# True  ✅
    
    print(register_values()) 						# [0, 0, 0, 0, 0] ✅
    
    print(run_program(x))							# False ✅ ❗
                # False due to missing "halt"
    
    print(register_values()) 						# [0, 0, 0, 0, 0] ✅
    
    
################### TEST 4: Run Program: Extreme Values ######################
    
if test == 4:
    
    x = ["set r100 to 1000000","set r10 to 500000","set r482 to 010010000110100100100000","divide r10 by r100","halt"]
    print(init(500))								# True  ✅
    
    print(run_program(x))							# True  ✅
    
    print(register_values()) # Massive list that I am NOT writing
    
    print(program_counter()) # 4
    
    x = ["set r100 to 1000000","set r10 to 500000","set r482 to 010010000110100100100000","multiply r10 by r100","if r10 goto 3","halt"]
    print(init(500))								# True  ✅
    
    print(run_program(x)) # Should be stuck forever
    
    print(register_values()) # ^^^^^^^^^^^^^^^^^^^^
    
    print(program_counter()) # ^^^^^^^^^^^^^^^^^^^^
    
    
    
    