from bnetbase import *
from carDiagnosis import *

if __name__ == '__main__':
    ## Question 1
    ## Car starts is independent of Air Filter given Air System.
    #asys.set_evidence('okay')
    #probs = VE(car, st, [asys])
    #for i in range(len(probs)):
        #print("P({0:} = {1:}) = {2:0.1f}".format(st.name, st.domain()[i], 100*probs[i]))
    #print()

    #asys.set_evidence('okay')
    #af.set_evidence('clean')
    #probs = VE(car, st, [asys, af])
    #for i in range(len(probs)):
        #print("P({0:} = {1:}) = {2:0.1f}".format(st.name, st.domain()[i], 100*probs[i]))
    #print()

    ## Question 2
    ## Voltage at Plug = 'weak' explains away Spark Quality = 'bad'
    ## which decreases the probability of Spark Plugs = 'too wide'
    ## and Spark Plugs = 'fouled'
    #sq.set_evidence('bad')
    #probs = VE(car, sp, [sq])
    #for i in range(len(probs)):
        #print("P({0:} = {1:}) = {2:0.1f}".format(sp.name, sp.domain()[i], 100*probs[i]))
    #print()

    #sq.set_evidence('bad')
    #pv.set_evidence('weak')
    #probs = VE(car, sp, [sq, pv])
    #for i in range(len(probs)):
        #print("P({0:} = {1:}) = {2:0.1f}".format(sp.name, sp.domain()[i], 100*probs[i]))
    #print()

    ## Question 3
    #probs = VE(car, st, [])
    #for i in range(len(probs)):
        #print("P({0:} = {1:}) = {2:0.1f}".format(st.name, st.domain()[i], 100*probs[i]))
    #print()

    ## asys = 'okay' increases the probability of 'Car Starts'
    #asys.set_evidence('okay')
    #probs = VE(car, st, [asys])
    #for i in range(len(probs)):
        #print("P({0:} = {1:}) = {2:0.1f}".format(st.name, st.domain()[i], 100*probs[i]))
    #print()

    ## fs = 'okay' increases the probability of 'Car Starts'
    #asys.set_evidence('okay')
    #fs.set_evidence('okay')
    #probs = VE(car, st, [asys, fs])
    #for i in range(len(probs)):
        #print("P({0:} = {1:}) = {2:0.1f}".format(st.name, st.domain()[i], 100*probs[i]))
    #print()

    ## cc = 'true' increases the probability of 'Car Starts'
    #asys.set_evidence('okay')
    #fs.set_evidence('okay')
    #cc.set_evidence('true')
    #probs = VE(car, st, [asys, fs, cc])
    #for i in range(len(probs)):
        #print("P({0:} = {1:}) = {2:0.1f}".format(st.name, st.domain()[i], 100*probs[i]))
    #print()

    ## sq = 'good' increases the probability of 'Car Starts'
    #asys.set_evidence('okay')
    #fs.set_evidence('okay')
    #cc.set_evidence('true')
    #sq.set_evidence('good')
    #probs = VE(car, st, [asys, fs, cc, sq])
    #for i in range(len(probs)):
        #print("P({0:} = {1:}) = {2:0.1f}".format(st.name, st.domain()[i], 100*probs[i]))
    #print()

    ## Question 4
    #probs = VE(car, cc, [])
    #for i in range(len(probs)):
        #print("P({0:} = {1:}) = {2:0.1f}".format(cc.name, cc.domain()[i], 100*probs[i]))
    #print()

    ## h1 = 'off' decreases the probability of 'Car Cranks'
    #hl.set_evidence('off')
    #probs = VE(car, cc, [hl])
    #for i in range(len(probs)):
        #print("P({0:} = {1:}) = {2:0.1f}".format(cc.name, cc.domain()[i], 100*probs[i]))
    #print()

    ## cs = 'faulty' decreases the probability of 'Car Cranks'
    #hl.set_evidence('off')
    #cs.set_evidence('faulty')
    #probs = VE(car, cc, [hl, cs])
    #for i in range(len(probs)):
        #print("P({0:} = {1:}) = {2:0.1f}".format(cc.name, cc.domain()[i], 100*probs[i]))
    #print()

    ## bv = 'strong' increases the probability of 'Car Cranks'
    #hl.set_evidence('off')
    #cs.set_evidence('faulty')
    #bv.set_evidence('strong')
    #probs = VE(car, cc, [hl, cs, bv])
    #for i in range(len(probs)):
        #print("P({0:} = {1:}) = {2:0.1f}".format(cc.name, cc.domain()[i], 100*probs[i]))
    #print()

    ## ss = 'okay' increases the probability of 'Car Cranks'
    #hl.set_evidence('off')
    #cs.set_evidence('faulty')
    #bv.set_evidence('strong')
    #ss.set_evidence('okay')
    #probs = VE(car, cc, [hl, cs, bv, ss])
    #for i in range(len(probs)):
        #print("P({0:} = {1:}) = {2:0.1f}".format(cc.name, cc.domain()[i], 100*probs[i]))
    #print()
