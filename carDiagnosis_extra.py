from carDiagnosis import *

if __name__ == '__main__':
    ba.set_evidence('old')
    sp.set_evidence('okay')
    tm.set_evidence('bad')
    ss.set_evidence('okay')
    prob = VE(car, st, [ba,sp,tm,ss])
    print("P(st = true | ba = old, sp = okay, tm = bad ss = okay) = {}\nP(st = false | ba = old, sp = okay, tm = bad ss = okay) = {} ".format(prob[0],prob[1]))
    

    #NOTE: in this example the evidence is impossible. 'cs' can't be
    #'okay' when 'al' is faulty. So we are conditioning on evidence
    #that has zero probability. (The conditional probability will
    #involve a division by zero).
    #
    #In the VE code what should happen is that the product of factors
    #over the query varible will yield a zero factor (i.e., all values
    #in the factor will be zero). Normalization will involve dividing
    #by the sum, which is a division by zero.
    #
    #That the unnormalized numbers are all zero indicates that the the
    #evidence has zero probability (the sum of the unnormalized
    #numbers in the final factor over the query variable is precisely
    #the probability of the evidence)
    #
    #You WILL NOT be tested on this case. But you can catch it by
    #testing your final distribution before normalizing. If it sums to
    #zero, you can return a vector of float('inf') which is python's
    #representation of infinity.

    cs.set_evidence('okay')
    al.set_evidence('faulty')
    prob = VE(car,bv, [cs, al])
    print("P(bv = strong | cs = okay, al = faulty ) = {}\nP(bv = weak | cs = okay, al = faulty )= {},\nP(bv = dead | cs = okay, al = faulty ) = {}".format(prob[0],prob[1], prob[2]))
