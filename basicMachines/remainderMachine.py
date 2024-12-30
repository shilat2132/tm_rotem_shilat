import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tm import Tm


class remainderPQ(Tm):


    def __init__(self, tapes):

        states = {"start", "q1", "back", "remainder"}


        deltaTable = {
            # start -> acc
            ("start", "_", "_", "_"): {"newState": "acc", "write": ["_", "_", "_"], "movement": ['S', 'S', 'S']},
            ("start", "1", "_", "_"): {"newState": "acc", "write": ["1", "_", "_"], "movement": ['S', 'S', 'S']},

            # start -> q1
            ("start", "1", "1", "_"): {"newState": "q1", "write": ["1*", "1", "_"], "movement": ['R', 'R', 'S']},

            # q1 -> acc
            ("q1", "_", "_", "_"): {"newState": "acc", "write": ["_", "_", "_"], "movement": ['S', 'S', 'S']},
            
            # q1 -> q1
            ("q1", "1", "1", "_"): {"newState": "q1", "write": ["1", "1", "_"], "movement": ['R', 'R', 'S']},

            # q1-> back
            ("q1", "1", "_", "_"): {"newState": "back", "write": ["1", "_", "_"], "movement": ['S', 'L', 'S']},

            # q1 -> remainder
            ("q1", "_", "1", "_"): {"newState": "remainder", "write": ["_", "1", "_"], "movement": ['L', 'S', 'S']},


            # back -> back
            ("back", "1", "1", "_"): {"newState": "back", "write": ["1", "1", "_"], "movement": ['S', 'L', 'S']},

            # back -> start
            ("back", "1", "_", "_"): {"newState": "start", "write": ["1", "_", "_"], "movement": ['S', 'R', 'S']},
            
            # remainder -> remainder
            ("remainder", "1", "1", "_"): {"newState": "remainder", "write": ["1", "1", "1"], "movement": ['L', 'S', 'R']},

            # remainder -> acc
            ("remainder", "1*", "1", "_"): {"newState": "acc", "write": ["1*", "1", "1"], "movement": ['S', 'S', 'S']}
           
            

        }


        super().__init__(tapes, states, "start", deltaTable, 3)    