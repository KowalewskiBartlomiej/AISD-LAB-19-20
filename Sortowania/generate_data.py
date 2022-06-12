import random

def draw_data(n,a,b):
    ans = []
    for i in range(n):
        ans.append(round(random.uniform(a,b)))
    return ans