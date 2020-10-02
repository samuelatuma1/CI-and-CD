def square(x):
    return x+x

#print(square(5) == 25)
#assert square(5) == 25

def squares(x):
     box =[]
     for a in x:
        b = a * a
        box.append(b)
     return box

print(squares([1,2,3,4,5]))
     
