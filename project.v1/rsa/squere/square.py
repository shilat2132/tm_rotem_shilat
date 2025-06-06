from basicMachines.mulMachine import mulMachine
from basicMachines.remainderMachine import remainderMachine
from utils import getHeadIndex
from .binaryMachine import binary
from tm import Tm


class SquereM(Tm):
    """
        a class for Exponentiation by Squaring.
        - has 5 tapes
        - gets the input in the tapes of: [x, b, n] 
        - computes (x^b) % n and stores the result in y, i.e the fifth tape
        - tapes = [x, b, n, m, y]
    """

    def __init__(self, tapes):

        deltaTable ={
            # q0 -> q0
            ("q0", "1", "0", "1", "_", "_") : {"newState": "q0",  "movement": ['S', 'R', 'S', 'S', 'S']},
            ("q0", "1", "1", "1", "_", "_") : {"newState": "q0",  "movement": ['S', 'R', 'S', 'S', 'S']},

            # q0 -> initY
            ("q0", "1", "_", "1", "_", "_") : {"newState": "initY",  "movement": ['S', 'L', 'S', 'S', 'S']},

            # initY -> remainder0
            ("initY", "1", "1", "1", "_", "_") : {"newState": "remainder0",  "movement": ['S', 'L', 'S', 'S', 'S']},

            # initY -> initM
            ("initY", "1", "0", "1", "_", "_") : {"newState": "initM", "write": ["1", "0", "1" , '_', '1'], "movement": ['S', 'L', 'S', 'S', 'S']}, 

             # remainderO -> initM
             

            # initM -> acc  
            ("initM", "1", "_", "1", "_", "1") : {"newState": "acc",  "movement": ['S', 'S', 'S', 'S', 'S']},

            # initM -> copyM
            ("initM", "1", "0", "1", "_", "1") : {"newState": "copyM",  "movement": ['S', 'S', 'S', 'S', 'S']},
            ("initM", "1", "1", "1", "_", "1") : {"newState": "copyM",  "movement": ['S', 'S', 'S', 'S', 'S']},

            # copyM -> loop


            # loop -> checkCond
            ("loop", "1", "0", "1", "1", "1") : {"newState": "checkCond",  "movement": ['S', 'L', 'S', 'S', 'S']}, 

            # loop -> updateY
            ("loop", "1", "1", "1", "1", "1") : {"newState": "updateY",  "movement": ['S', 'L', 'S', 'S', 'S']},

            # checkCond -> loop
            ("checkCond", "1", "0", "1", "1", "1") : {"newState": "loop",  "movement": ['S', 'S', 'S', 'S', 'S']},
            ("checkCond", "1", "1", "1", "1", "1") : {"newState": "loop",  "movement": ['S', 'S', 'S', 'S', 'S']},

            #checkCond -> acc
            ("checkCond", "1", "_", "1", "1", "1") : {"newState": "acc",  "movement": ['S', 'S', 'S', 'S', 'S']},


        }

        super().__init__(tapes, "bin", deltaTable, 5)


    
    def runMachine(self):
        # self.tapes = [x, b, n, m, y]
        i=0
        while self.currentState != "acc":
            
            if self.currentState == "bin":
                b1, config = binary(self.tapes[1]) #b1 = bin(b)
                self.tapes[1] = b1
                self.pos[1] = getHeadIndex(self.tapes[1])
                # Tm.copyTape(b1, self.tapes[1]) # b = b1= bin(b)
                self.currentState = "q0"

            elif self.currentState == "remainder0":
                tapes = [self.tapes[0], self.tapes[2], self.tapes[4]] #tapes = [x, n, y]
                remainderM = remainderMachine(tapes)
                remainderM.runMachine() #y=x%n
                self.currentState = "initM"

            elif self.currentState == "copyM":
                Tm.copyTape(self.tapes[0], self.tapes[3]) # m = x
                self.currentState = "loop"

            elif self.currentState == "loop":
                print(f"i={i}")
                i+=1
                # raise m to the power of 2
                t1, t2 = self.tapes[3].copy(), self.tapes[3].copy() #t1=t2=m
                mulM = mulMachine([t1, t2, self.tapes[3]]) #m =t1*t2 = m^2
                mulM.runMachine()

                # compute the mod of m^2
                tapes = [self.tapes[3], self.tapes[2], self.tapes[3]] #tapes = [m, n, m]
                remainderM = remainderMachine(tapes) #m = m%n
                remainderM.runMachine()
                self.step() #activate the transition in the delta table
            
            elif self.currentState=="updateY":
                    # compute y = (y*m)%n
                # compute y=y*m
                tapes = [self.tapes[4].copy(), self.tapes[3], self.tapes[4]] #tapes = [y, m, y]
                mulM = mulMachine(tapes) #y = y*m
                mulM.runMachine()

                # compute y = y%n
                remainderM = remainderMachine([self.tapes[4], self.tapes[2], self.tapes[4]]) #tapes = [y, n, y]
                remainderM.runMachine() #y = y%n
                self.currentState = "checkCond"
            
            else:
                self.step()


    def result(self):
        return self.tapes[4]



