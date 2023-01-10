theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def check(value):
    if value == 1:
        return 'wiki'
    else:
        return 'woko'

result = list(map(check, theBools))
print(result)