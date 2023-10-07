# you can add imports but you should not rely on libraries that are not already provided in "requirements.txt #
from heapq import heappush, heappop
from lab2_utils import TextbookStack, apply_sequence
from collections import deque

def is_goal(stack, flip_sequence):
    new_stack = apply_sequence(stack, flip_sequence)
    return new_stack.check_ordered()

def expand(flip_sequence, num_books):
    expanded = []
    # expand the current flip through every position
    for next in range(1, num_books+1):
        now_seq = flip_sequence.copy()
        now_seq.append(next)
        expanded.append(now_seq)
    return expanded

def build_state(stack):
    #return tuple([tuple(stack.order), tuple(stack.orientations)])
    return tuple(list(stack.order)+list(stack.orientations))

def cal_h(stack):
    order = stack.order
    orientation = stack.orientations
    pairs = set()
    for i in range(stack.num_books-1):
        # case 1
        if (order[i] != order[i+1]+1) and (order[i] != order[i+1]-1):
            pairs.add((order[i], order[i+1]))
        # case 2
        if (orientation[i] != orientation[i+1]):
            pairs.add((order[i], order[i+1]))
        # case 3
        if ((orientation[i] == 1) and (orientation[i+1] == 1)) and (order[i] > order[i+1]):
            pairs.add((order[i], order[i+1]))
        # case 4
        if ((orientation[i] == 0) and (orientation[i+1] == 0)) and (order[i] < order[i+1]):
            pairs.add((order[i], order[i+1]))
    return len(pairs)

def a_star_search(stack):
    # each element in a heap
    # [f, g, sequence]
    flip_sequence = []
    heap = []
    reached = set()
    # initial
    if is_goal(stack, flip_sequence):
        return flip_sequence
    init_h = cal_h(apply_sequence(stack, []))
    # [g+h, g, seq]
    heappush(heap, [init_h + 0, 0, []])
    while(len(heap)!=0):
        now = heappop(heap)
        now_g = now[1]
        now_seq = now[2]
        now_state = build_state(apply_sequence(stack, now_seq))
        if now_state in reached:
            continue
        reached.add(now_state)
        if is_goal(stack, now_seq):
            return now_seq
        expanded = expand(now_seq, stack.num_books)
        for child_seq in expanded:
            child_h = cal_h(apply_sequence(stack, child_seq))
            child_f = now_g+1 + child_h
            heappush(heap, [child_f, now_g+1, child_seq])
    print('ans not found')
    return False


def weighted_a_star_search(stack, epsilon=None, N=1):
    # Weighted A* is extra credit

    flip_sequence = []

    # --- v ADD YOUR CODE HERE v --- #

    return flip_sequence

    # ---------------------------- #
