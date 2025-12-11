# stack single
stack = []

# push
stack.append(10)
stack.append(20)
stack.append(30)

# pop
stack.pop()  # menghapus 30


# stack double
size = 10
array = [None] * size
top1 = -1         # stack 1 mulai dari kiri
top2 = size       # stack 2 mulai dari kanan

def push1(value):
    global top1
    if top1 + 1 == top2:
        return "Stack penuh"
    top1 += 1
    array[top1] = value

def push2(value):
    global top2
    if top1 + 1 == top2:
        return "Stack penuh"
    top2 -= 1
    array[top2] = value
