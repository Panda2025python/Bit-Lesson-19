def max_mid(n):
    arr = [-1,n,-1]
    current = best = arr[0]
    for x in arr[1:]:
        if current < 0: current = x 
        else:current = current + x
        if current > best: best = current
    return best
print("max_mid(3) =", max_mid(3))
print("max_mid(4) =", max_mid(4))
n = int(input("Enter number"))
print("Max_mid of" + str(n) + "=", max_mid(n))