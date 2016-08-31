def primitive(state):
    if state == 0:
        return 'L'
    return 'U'

def init_pos():
    return 4

def do_move(state, action):
    return state + action

def gen_moves(state):
    if state == 1:
        return [-1]
    return [-1,-2]

#solves, does not account for draws or loops
def solve():
    state_sols = {}
    def evaluate(s):
        def mem_and_return(v):
            state_sols[str(s)] = v
            return v

        if str(s) in state_sols:
            return state_sols[str(s)]
        p = primitive(s)
        if p != 'U':
            return mem_and_return(p)

        successors_vals = set()
        actions = gen_moves(s)
        for action in actions:
            successor = do_move(s, action)
            successor_val = evaluate(successor)
            successors_vals.add(successor_val)
        if 'L' in successors_vals:
            return mem_and_return('W')
        if 'T' in successors_vals:
            return mem_and_return('T')
        return mem_and_return('L')

    initial_pos = init_pos()
    evaluate(initial_pos)
    return state_sols

print solve()