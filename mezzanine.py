import math
#adenine represents 00, cytosine represents 01, guanine represents 10 and thymine represents 11.
z = input('In or Out? i/o - ')
if z == "o":
    A = input('DNA here pls - ')
    #space out dna every 1 character
    B = ' '.join(A[i:i+1] for i in range(0, len(A), 1))
    #replacements
    C = B.replace("G", "10")
    D = C.replace("A", "00")
    E = D.replace("C", "01")
    F = E.replace("T", "11")
    G = F.replace(" ", "")
    #space out binary every 8 characters
    H = ' '.join(G[i:i+8] for i in range(0, len(G), 8))
    print(H)
    #convert binary to unicode
    J = ''.join([chr(int(bc, 2)) for bc in H.split(' ')])
    print(J)

if z == "i":
    j = input('Words here pls - ')
    #convert to binary
    k = "".join(f"{ord(i):08b}" for i in j)
    print(k)
    #add a space every 2 characters
    l = ' '.join(k[i:i+2] for i in range(0, len(k), 2))
    m=l.replace("10", "G")
    n=m.replace("00", "A")
    o=n.replace("01", "C")
    p=o.replace("11", "T")
    q=p.replace(" ", "")
    print(q)
    
else:
    print("Invalid choice")

