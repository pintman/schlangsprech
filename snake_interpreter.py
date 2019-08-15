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
    regs = [0] * 10
    tick, max_ticks = 0, 100
    
    while tick < max_ticks and pc < len(lines):
        tick += 1
        cmd, arg = extract_cmd_arg(lines[pc])
        print("pc: %s reg: %s regs: %s dir: %s @%s" % 
            (pc, reg, regs, current_direction, lines[pc]))
        if cmd == 'nop':
            pass
        elif cmd == 'sense': 
            reg = sense()
        elif cmd == 'sub1': 
            reg -= 1
        elif cmd == 'add1': 
            reg += 1
        elif cmd == 'copyto':
            regs[int(arg)] = reg
        elif cmd == 'copyfrom':
            reg = regs[int(arg)]
        elif cmd == 'ifn':
            if reg < 0:
                pc += int(arg)
                continue
        elif cmd == 'ifz':
            if reg == 0:
                pc += int(arg)
                continue
        elif cmd == 'jmp':
            pc += int(arg)
            continue
        elif cmd == 'left': 
            turn_left()
        elif cmd == 'right': 
            turn_right()
        else:
            raise Exception('Command unknown', cmd)
            
        pc += 1

def extract_cmd_arg(cmd_arg):
    'take the userinput and extract cmd and argument.'
    cmd2 = cmd_arg.lower().strip()
    if ' ' in cmd2:
        c, a = cmd2.split(' ')
        return c, a
    else:
        return cmd2, None

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

def demo5():
    'rememering last sensed'
    prog = '''sense
    copyto 1
    add1
    copyto 2
    add1
    copyto 3
    copyfrom 1
    sub1
    nop'''

    print(prog)
    interpret(prog)

if __name__ == '__main__':
    print("Starting")
    demo5()