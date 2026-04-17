def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L) # What is the value of test on each call? First call: False Second call: True
    if test: # What is this check preventing? An Index Error
        return L[idx]
    else:
        return None

first = checked_access([1, 0, 1], 9) # What is the value of first? None
second = checked_access([1, 0, 1], 2) # What is the value of second? 1
print()