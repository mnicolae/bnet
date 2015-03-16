##Two sample bayes nets are defined here. 
##
from bnetbase import *

VisitAsia = Variable('Visit_To_Asia', ['visit', 'no-visit'])
F1 = Factor("F1", [VisitAsia])
F1.add_values([['visit', 0.01], ['no-visit', 0.99]])

Smoking = Variable('Smoking', ['smoker', 'non-smoker'])
F2 = Factor("F2", [Smoking])
F2.add_values([['smoker', 0.5], ['non-smoker', 0.5]])

Tuberculosis = Variable('Tuberculosis', ['present', 'absent'])
F3 = Factor("F3", [Tuberculosis, VisitAsia])
F3.add_values([['present', 'visit', 0.05],
               ['present', 'no-visit', 0.01],
               ['absent', 'visit', 0.95],
               ['absent', 'no-visit', 0.99]])

Cancer = Variable('Lung Cancer', ['present', 'absent'])
F4 = Factor("F4", [Cancer, Smoking])
F4.add_values([['present', 'smoker', 0.10],
               ['present', 'non-smoker', 0.01],
               ['absent', 'smoker', 0.90],
               ['absent', 'non-smoker', 0.99]])

Bronchitis = Variable('Bronchitis', ['present', 'absent'])
F5 = Factor("F5", [Bronchitis, Smoking])
F5.add_values([['present', 'smoker', 0.60],
               ['present', 'non-smoker', 0.30],
               ['absent', 'smoker', 0.40],
               ['absent', 'non-smoker', 0.70]])

TBorCA = Variable('Tuberculosis or Lung Cancer', ['true', 'false'])
F6 = Factor("F6", [TBorCA, Tuberculosis, Cancer])
F6.add_values([['true', 'present', 'present', 1.0],
               ['true', 'present', 'absent', 1.0],
               ['true', 'absent', 'present', 1.0],
               ['true', 'absent', 'absent', 0],
               ['false', 'present', 'present', 0],
               ['false', 'present', 'absent', 0],
               ['false', 'absent', 'present', 0],
               ['false', 'absent', 'absent', 1]])


Dyspnea = Variable('Dyspnea', ['present', 'absent'])
F7 = Factor("F7", [Dyspnea, TBorCA, Bronchitis])
F7.add_values([['present', 'true', 'present', 0.9],
               ['present', 'true', 'absent', 0.7],
               ['present', 'false', 'present', 0.8],
               ['present', 'false', 'absent', 0.1],
               ['absent', 'true', 'present', 0.1],
               ['absent', 'true', 'absent', 0.3],
               ['absent', 'false', 'present', 0.2],
               ['absent', 'false', 'absent', 0.9]])


Xray = Variable('XRay Result', ['abnormal', 'normal'])
F8 = Factor("F8", [Xray, TBorCA])
F8.add_values([['abnormal', 'true', 0.98],
               ['abnormal', 'false', 0.05],
               ['normal', 'true', 0.02],
               ['normal', 'false', 0.95]])

Asia = BN("Asia", [VisitAsia, Smoking, Tuberculosis, Cancer,
                   Bronchitis, TBorCA, Dyspnea, Xray],
                   [F1, F2, F3, F4, F5, F6, F7, F8])

## E,B,S,w,G example from sample questions
E = Variable('E', ['e', '-e'])
B = Variable('B', ['b', '-b'])
S = Variable('S', ['s', '-s'])
G = Variable('G', ['g', '-g'])
W = Variable('W', ['w', '-w'])
FE = Factor('P(E)', [E])
FB = Factor('P(B)', [B])
FS = Factor('P(S|E,B)', [S, E, B])
FG = Factor('P(G|S)', [G,S])
FW = Factor('P(W|S)', [W,S])

FE.add_values([['e',0.1], ['-e', 0.9]])
FB.add_values([['b', 0.1], ['-b', 0.9]])
FS.add_values([['s', 'e', 'b', .9], ['s', 'e', '-b', .2], ['s', '-e', 'b', .8],['s', '-e', '-b', 0],
               ['-s', 'e', 'b', .1], ['-s', 'e', '-b', .8], ['-s', '-e', 'b', .2],['-s', '-e', '-b', 1]])
FG.add_values([['g', 's', 0.5], ['g', '-s', 0], ['-g', 's', 0.5], ['-g', '-s', 1]])
FW.add_values([['w', 's', 0.8], ['w', '-s', .2], ['-w', 's', 0.2], ['-w', '-s', 0.8]])

Q3 = BN('SampleQ4', [E,B,S,G,W], [FE,FB,FS,FG,FW])


if __name__ == '__main__':
    #(a)
    print("Question 5a")
    G.set_evidence('g')
    probs = VE(Q3, S, [G])
    print('P(s|g) = {} P(-s|g) = {}'.format(probs[0], probs[1]))

    #(b)
    print("\nQuestion 5b")
    B.set_evidence('b')
    E.set_evidence('-e')
    probs = VE(Q3, W, [B, E])
    print('P(w|b,-e) = {} P(-w|b,-e) = {}'.format(probs[0],probs[1]))

    #(c)
    print("\nQuestion 5c")
    S.set_evidence('s')
    probs1 = VE(Q3, G, [S])
    S.set_evidence('-s')
    probs2 = VE(Q3, G, [S])
    print('P(g|s) = {} P(-g|s) = {} P(g|-s) = {} P(-g|-s) = {}'.format(probs1[0],probs1[1],probs2[0],probs2[1]))

    #(d)
    print("\nQuestion 5d")
    S.set_evidence('s')
    W.set_evidence('w')
    probs1 = VE(Q3, G, [S,W])
    S.set_evidence('s')
    W.set_evidence('-w')
    probs2 = VE(Q3, G, [S,W])
    S.set_evidence('-s')
    W.set_evidence('w')
    probs3 = VE(Q3, G, [S,W])
    S.set_evidence('-s')
    W.set_evidence('-w')
    probs4 = VE(Q3, G, [S,W])
    print('P(g|s,w) = {} P(-g|s,w) = {} P(g|s,-w) = {} P(-g|s,-w) = {}'.format(probs1[0],probs1[1],probs2[0],probs2[1]))
    print('P(g|-s,w) = {} P(-g|-s,w) = {} P(g|-s,-w) = {} P(-g|-s,-w) = {}'.format(probs3[0],probs3[1],probs4[0],probs4[1]))

    #(e)
    print("\nQuestion 5e")
    print('Since P(G|S,W) = P(G|S) (i.e., this equation holds for every value of G, S, and W)')
    print('we have that G is conditionally independent of W given S.')
    
    #(f) 
    print("\nQuestion 5f")
    W.set_evidence('w')
    probs1 = VE(Q3, G, [W])
    W.set_evidence('-w')
    probs2 = VE(Q3, G, [W])
    print('P(g|w) = {} P(-g|w) = {} P(g|-w) = {} P(-g|-w) = {}'.format(probs1[0],probs1[1],probs2[0],probs2[1]))

    #(g) 
    print("\nQuestion 5g")
    print('Since the probability of G changes as we change the value of W, G is not independent of W')
    print('However d and e show that given S G becomes independent of W')


    #(h)
    print("\nExtra Note")
    print("VE can compute the unconditional probability of a variable by selecting no evidence variables")
    probs = VE(Q3, G, [])
    print('P(g) = {} P(-g) = {}'.format(probs[0], probs[1]))
    probs = VE(Q3, E, [])
    print('P(e) = {} P(-e) = {}'.format(probs[0], probs[1]))
    print("\nNow you can experiment with the Asia network")

