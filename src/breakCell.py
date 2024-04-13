'''Functions to delete molecules'''

import numpy as np
import TurtleMol as tm

def breakMol(struc, iParams):
    '''Deletes molecules based on defined parameters'''

    deleteNum = int(len(struc) * iParams['remove']/100)

    # Generate random indicies for the atoms to delete
    idx2Delete = np.random.choice(len(struc), deleteNum, replace=False)

    # Create a new list excluding the indicies to delete
    newCoords = [struc[i] for i in range(len(struc)) if i not in deleteNum]

    return newCoords, 'molecule'