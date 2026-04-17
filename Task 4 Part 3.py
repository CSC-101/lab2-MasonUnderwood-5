def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
         # What is the value of words at this point? ["this", "is", "confusing", "code.", AVOID", "SUCH."]
         # What are the values of first and second at this point? The values of first and second are the same ["this", "is", "confusing", "code.", AVOID", "SUCH."]
         # What happened? They all point to the same object which is list called words
print()