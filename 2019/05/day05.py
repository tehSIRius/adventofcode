def intcode(program):
    i = 0

    while i < len(program):
        opcode = 0
        breakdown = [int(x) for x in str(program[i])]

        breakdown.reverse()

        opcode = int(breakdown[0])

        if len(breakdown) > 1:
            opcode += 10 * int(breakdown[1])

        value_a = 0
        value_b = 0
        mode_a = 0
        mode_b = 0
        mode_c = 0
        position = 0

        print('Instruction is %s' % opcode)

        if opcode == 99 or opcode == 0:
            break

        if len(breakdown) > 2:
            mode_a = breakdown[2]
        
        if len(breakdown) > 3:
            mode_b = breakdown[3]
        
        if len(breakdown) > 4:
            mode_c = breakdown[4]

        print('Modes are A:%s B:%s C:%s' % (mode_a, mode_b, mode_c))

        if mode_a:
            value_a = program[i + 1]
        else:
            value_a = program[program[i + 1]]

        if opcode != 3 and opcode != 4:
            if mode_b:
                value_b = program[i + 2]
            else:
                value_b = program[program[i + 2]]
        
        if mode_c:
            position = i + 3
        else:
            position = program[i + 3]

        if opcode == 1:
            print('Adding together values %s and %s to position %s' % (value_a, value_b, position))
            program[position] = int(value_a) + int(value_b)
            i += 4
        elif opcode == 2:
            print('Multiplication of values %s and %s to position %s' % (value_a, value_b, position))
            program[position] = int(value_a) * int(value_b)
            i += 4
        elif opcode == 3:
            print('Requesting value to %s' % position)
            program[position] = input('Input value is: ')
            i += 2
        elif opcode == 4:
            print('Returning a value of %s from %s' % (value_a, position))
            i += 2
        elif opcode == 5:
            print('Jump-if-true for %s' % value_a)
            if int(value_a) != 0:
                i = int(value_b)
            else:
                i += 3
        elif opcode == 6:
            print('Jump-if-false for %s' % value_a)
            if int(value_a) == 0:
                i = int(value_b)
            else:
                i += 3
        elif opcode == 7:
            print('Comparing %s < %s to %s' % (value_a, value_b, position))
            if int(value_a) < int(value_b):
                program[position] = 1
            else:
                program[position] = 0
            
            i += 4
        elif opcode == 8:
            print('Comparing %s == %s to %s' % (value_a, value_b, position))
            if int(value_a) == int(value_b):
                program[position] = 1
            else:
                program[position] = 0
            
            i += 4

if __name__ == "__main__":
    main_program = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,68,5,225,1101,71,12,225,1,117,166,224,1001,224,-100,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1001,66,36,224,101,-87,224,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1101,26,51,225,1102,11,61,224,1001,224,-671,224,4,224,1002,223,8,223,1001,224,5,224,1,223,224,223,1101,59,77,224,101,-136,224,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,1101,11,36,225,1102,31,16,225,102,24,217,224,1001,224,-1656,224,4,224,102,8,223,223,1001,224,1,224,1,224,223,223,101,60,169,224,1001,224,-147,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1102,38,69,225,1101,87,42,225,2,17,14,224,101,-355,224,224,4,224,102,8,223,223,1001,224,2,224,1,224,223,223,1002,113,89,224,101,-979,224,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1102,69,59,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,7,677,677,224,1002,223,2,223,1006,224,329,1001,223,1,223,1007,226,226,224,1002,223,2,223,1006,224,344,1001,223,1,223,1108,226,677,224,102,2,223,223,1005,224,359,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,374,101,1,223,223,1107,677,226,224,1002,223,2,223,1006,224,389,101,1,223,223,7,226,677,224,1002,223,2,223,1005,224,404,101,1,223,223,1008,677,226,224,102,2,223,223,1005,224,419,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,434,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,449,1001,223,1,223,108,226,677,224,102,2,223,223,1005,224,464,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,479,101,1,223,223,1007,226,677,224,102,2,223,223,1006,224,494,101,1,223,223,107,677,677,224,102,2,223,223,1005,224,509,101,1,223,223,108,677,677,224,102,2,223,223,1006,224,524,1001,223,1,223,8,226,677,224,102,2,223,223,1005,224,539,101,1,223,223,107,677,226,224,102,2,223,223,1005,224,554,1001,223,1,223,8,226,226,224,102,2,223,223,1006,224,569,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,584,1001,223,1,223,1108,226,226,224,102,2,223,223,1005,224,599,1001,223,1,223,1107,677,677,224,1002,223,2,223,1006,224,614,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,629,1001,223,1,223,108,226,226,224,102,2,223,223,1005,224,644,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,659,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226]


    test_program = [3,9,8,9,10,9,4,9,99,-1,8]

    test_result = intcode(test_program)

    if not test_result:
        print('Test program passed successfully')
        print('Moving to main program')

        main_result = intcode(main_program)
    else:
        print('Test program failed')
