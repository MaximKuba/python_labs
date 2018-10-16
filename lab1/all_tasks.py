print("hello world!")

def func(a, b):
    if a < 0 or b < 0:
        raise Exception("Wrong input")
        
    if a % b == 0:
        return True
    else:
        return False
    

def func1(a, b):
    if a < 0 or b < 0:
        raise Exception("Wrong input")
    
    primes = []
    for x in range(a, b+1):
        count = 2
        for i in range(2, x):
            count += 1
            if x % i == 0:
                break
        if count == x and count != 2:
            primes.append(x)
        
    print(primes)
    
arr = ['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]

def a(arr):
    new_arr = []
    for i in arr:
        if type(i) == type([]):
            new_arr += a(i)
        else:
            new_arr.append(i)
    print(new_arr)
    
    
list=['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]
li=[[123,"rm"],[{2,4}]]

def flatten(aList):
    copyL = []
    for k in aList:
        if type(k) == type([]):
            copyL = copyL + flatten(k)
        else:
            copyL.append(k)
    return copyL
print(flatten(list))
print(flatten(li))

    