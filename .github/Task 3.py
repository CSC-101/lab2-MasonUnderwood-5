def smallest(n:float, m:float)->float:
    if n < m:
        return n # For which calls below is this statement evaluated? Neither
    else:
        return m

first=smallest(3,2) # What is the value of the first? 2
second=smallest(2,2) # What is the value of the second? Is this a reasonable result? 2 because the code returns m, so 2 is printed
print()
