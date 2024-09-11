import math
from collections import deque

a=int(input("Enter Jug A capacity: "))
b=int(input("Enter jug B capacity: "))
ai=int(input("Initially water in jug A: "))
bi=int(input("Initially water in jug B: "))
af=int(input("Final state of jug A: "))
bf=int(input("Final state of jug B: " ))

if a<=0 or b<=0:
    print("Jug Capacities must be positive.")
    exit(1)
if ai<0 or bi<0 or af<0 or bf<0:
    print("Negative value are not allowed.")
    exit(1)
if ai==af and bi==bf:
    print(f"initial state is already the final state:jug {ai} and jug{bi}")
    exit()

def bfs_wjug(a,b,ai,bi,af,bf):
    visited=set()
    queue=deque([(ai,bi,[])])

    while queue:
        curr_ai,curr_bi,operations=queue.popleft()
        if(curr_ai,curr_bi) in visited:
            continue
        visited.add((curr_ai,curr_bi))

        if curr_ai == af and curr_bi == bf:
            for i,op in enumerate(operations):
                print(f"step {i+1}: {op}")
            print(f"final state reached:Jug A ={curr_ai},Jug B={curr_bi}")
            return

        possible_operations=[
            (a,curr_bi,"Fill Jug A"),
            (curr_ai,b,"Fill Jug B"),
            (0,curr_bi,"Empty Jug A"),
            (curr_ai,0,"Empty Jug B"),
            (curr_ai-min(curr_ai,b-curr_bi),
             curr_bi+min(curr_ai,b-curr_bi),
             "pour from A to B"),
            (curr_ai+min(curr_bi,a-curr_ai),
             curr_bi-min(curr_bi,a-curr_ai),
             "pour from B to A"),
        ]

        for next_ai,next_bi,op in possible_operations:
            if (next_ai,next_bi) not in visited:
                queue.append((next_ai,next_bi,operations+[op]))
    print("No solution found.")
    return
gcd=math.gcd(a,b)

if (af<=a and bf<=b) and (af%gcd==bf%gcd==0):
    bfs_wjug(a,b,ai,bi,af,bf)
else:
    print("the final state is not achievable with the given capacities.")
    exit()








        
