def bubblesort(l):
    [l.append(l.pop(0) if i == len(l) - 1 or l[0] < l[1] else l.pop(1)) for j in range(0, len(l)) for i in range(0, len(l))]
    return l

print(bubblesort([1,67,4,434,6,6,7,1,9]))