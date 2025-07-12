#LVM


n = int(input())
instructions = [input().strip() for i in range(n)]

stack = []
register = 0
i = 0 

while i < n:
    parts = instructions[i].split()
    cmd = parts[0]
    if cmd == "PUSH":
        x = int(parts[1])
        stack.insert(0, x)
    elif cmd == "STORE":
        register = stack.pop(0)
    elif cmd == "LOAD":
        stack.insert(0, register)
    elif cmd == "PLUS":
        a = stack.pop(0)
        b = stack.pop(0)
        stack.insert(0, a + b)
    elif cmd == "TIMES":
        a = stack.pop(0)
        b = stack.pop(0)
        stack.insert(0, a * b)
    elif cmd == "IFZERO":
        jump_target = int(parts[1])
        top = stack.pop(0)
        if top == 0:
            i = jump_target
            continue  
    elif cmd == "DONE":
        print(stack[0])
        break

    i += 1


