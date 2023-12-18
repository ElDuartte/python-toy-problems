def find_short(s):
    words = s.split()
    minLeng = min(len(word) for word in words)
    return(minLeng)


find_short("bitcoin take over the world maybe who knows perhaps")
# find_short("turns out random test cases are easier than writing out basic ones")
