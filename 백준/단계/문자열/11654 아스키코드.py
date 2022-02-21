c = input()

try:
    map(int, c)
    print(chr(c))
except:
    print(ord(c))
