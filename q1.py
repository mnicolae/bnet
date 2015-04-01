from bnetbase import *

A = Variable('A', ['a', '-a'])
B = Variable('B', ['b', '-b'])
C = Variable('C', ['c', '-c'])
D = Variable('D', ['d', '-d'])
E = Variable('E', ['e', '-e'])
F = Variable('F', ['f', '-f'])
G = Variable('G', ['g', '-g'])
H = Variable('H', ['h', '-h'])
I = Variable('I', ['i', '-i'])

FA = Factor('P(A)',     [A])
FB = Factor('P(B|A,H)', [B, A, H])
FC = Factor('P(C|B,G)', [C, B, G])
FD = Factor('P(D|C,F)', [D, C, F])
FE = Factor('P(E|C)',   [E, C])
FF = Factor('P(F)',     [F])
FG = Factor('P(G)',     [G])
FH = Factor('P(H)',     [H])
FI = Factor('P(I|B)',   [I, B])

FA.add_values([['a', 0.9], ['-a', 0.1]])
FB.add_values([['b',  'a',  'h',  1.0], \
               ['b',  'a',  '-h', 0.0], \
               ['b',  '-a', 'h',  0.5], \
               ['b',  '-a', '-h', 0.6], \
               ['-b', 'a',  'h',  0.0], \
               ['-b', 'a',  '-h', 1.0], \
               ['-b', '-a', 'h',  0.5], \
               ['-b', '-a', '-h', 0.4]])
FC.add_values([['c',  'b',  'g',  0.9], \
               ['c',  'b',  '-g', 0.9], \
               ['c',  '-b', 'g',  0.1], \
               ['c',  '-b', '-g', 1.0], \
               ['-c', 'b',  'g',  0.1], \
               ['-c', 'b',  '-g', 0.1], \
               ['-c', '-b', 'g',  0.9], \
               ['-c', '-b', '-g', 0.0]])
FD.add_values([['d',  'c',  'f',  0.0], \
               ['d',  'c',  '-f', 1.0], \
               ['d',  '-c', 'f',  0.7], \
               ['d',  '-c', '-f', 0.2], \
               ['-d', 'c',  'f',  1.0], \
               ['-d', 'c',  '-f', 0.0], \
               ['-d', '-c', 'f',  0.3], \
               ['-d', '-c', '-f', 0.8]])
FE.add_values([['e',  'c',  0.2], \
               ['e',  '-c', 0.4], \
               ['-e', 'c',  0.8], \
               ['-e', '-c', 0.6]])
FF.add_values([['f', 0.1], ['-f', 0.9]])
FG.add_values([['g', 1.0], ['-g', 0.0]])
FH.add_values([['h', 0.5], ['-h', 0.5]])
FI.add_values([['i',  'b',  0.3], \
               ['i',  '-b',  0.9], \
               ['-i', 'b', 0.7], \
               ['-i', '-b', 0.1]])

Q1 = BN('Q1', [A,B,C,D,E,F,G,H,I], [FA,FB,FC,FD,FE,FF,FG,FH,FI])

if __name__ == '__main__':
    #(a)
    print("Question 1a")
    A.set_evidence('a')
    probs = VE(Q1, B, [A])
    print('P(b|a) = {} P(-b|a) = {}'.format(probs[0], probs[1]))

    #(b)
    print("Question 1b")
    A.set_evidence('a')
    probs = VE(Q1, C, [A])
    print('P(c|a) = {} P(-c|a) = {}'.format(probs[0], probs[1]))

    #(c)
    print("Question 1c")
    A.set_evidence('a')
    E.set_evidence('-e')
    probs = VE(Q1, C, [A,E])
    print('P(c|a,-e) = {} P(-c|a,-e) = {}'.format(probs[0], probs[1]))

    #(d)
    print("Question 1d")
    A.set_evidence('a')
    F.set_evidence('-f')
    probs = VE(Q1, C, [A,F])
    print('P(c|a,-f) = {} P(-c|a,-f) = {}'.format(probs[0], probs[1]))
