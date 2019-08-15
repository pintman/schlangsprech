directions = [[0, -1],  # ^
              [1, 0],   # >
              [0, 1],   # v
              [-1, 0]]  # <

current_direction = 0

def interpret(prog):
    'interpret the given program'
    global current_direction
    lines = prog.splitlines()
    pc = 0
    reg = 0  # register value
    tick, max_ticks = 0, 100
    
    while tick < max_ticks and pc < len(lines):
        tick += 1
        cmd = lines[pc].lower().strip()
        print("pc: %s reg: %s dir: %s \t @ %s" % (pc, reg, current_direction, cmd))
        if cmd == 'nop':
            pass
        elif cmd == 'sense': 
            reg = sense()
        elif cmd == 'sub1': 
            reg -= 1
        elif cmd == 'add1': 
            reg += 1
        elif cmd.startswith('ifn'):
            if reg < 0:
                pc += get_int_arg(cmd)
                continue
        elif cmd.startswith('ifz'):
            if reg == 0:
                pc += get_int_arg(cmd)
                continue
        elif cmd.startswith('jmp'):
            pc += get_int_arg(cmd)
            continue
        elif cmd == 'left': 
            turn_left()
        elif cmd == 'right': 
            turn_right()
        else:
            raise Exception('Command unknown', cmd)
            
        pc += 1

def get_arg(cmd):
    'Return the argument of CMD ARG.'
    return cmd.split(' ')[1]

def get_int_arg(cmd):
    'Return the ARG of CMD ARG as int.'
    return int(get_arg(cmd))

def turn_left():
    global current_direction
    current_direction = (current_direction - 1) % len(directions)

def turn_right():
    global current_direction
    current_direction = (current_direction + 1) % len(directions)

def sense():
    'Returning food pill in direction 0, 1, 2, 3 (^ > v >).'
    # TODO sensing dummy value
    import random
    return random.randrange(0, 3)

def demo1():
    prog = '''sense
    sub1
    ifn +2
    jmp -2
    nop
    left
    right
    right
    nop'''

    print("run prog:\n" + prog)
    interpret(prog)

def demo2():
    prog = '''sense
    sub1
    ifn +8
    sub1
    ifn +7
    sub1
    ifn +3
    sub1
    ifn +1
    left
    jmp +3
    right
    jmp -2
    nop'''
    interpret(prog)

def demo3():
    'looking for food pill left'
    prog = '''sense
    sub1
    ifz +2
    jmp +2
    left
    nop'''
    print(prog)
    interpret(prog)

def demo4():
    'searching for food pill.'
    prog = '''sense
    sub1
    ifn +8
    sub1
    ifn +7
    sub1
    ifn +3
    sub1
    ifn +1
    left
    jmp +3
    right
    jmp -2
    nop'''

    print(prog)
    interpret(prog)


if __name__ == '__main__':
    print("Starting")
    demo4()