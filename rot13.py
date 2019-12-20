from sys import argv

# filename for decrypt or encrypt
fn = argv[1]

def rot13(filename):

    with open(filename) as f:
        d = {}
        for c in (65, 97):
            for i in range(26):
                d[chr(i+c)] = chr((i+13) % 26 + c)
        s = f.read()
        
        print("".join([d.get(c, c) for c in s]))


rot13(fn)