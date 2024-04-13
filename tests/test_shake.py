from ShakeNBreak.shakeCell import shakeMol
from ShakeNBreak.utils import groupAtoms
import TurtleMol as tm

def testShake():
    iParams = {
        'structureFile' : 'tests/data/Water.xyz',
        'mode' : 'shake',
        'magnitude' : 0.1,
        'output' : 'tests/data/output.xyz'
    }


    struc, unitCell = tm.readStrucFile(iParams['structureFile']) # Converts pdb or xyz files in pandas dataframe

    if unitCell:
        iParams['unitCell'] = [unitCell['a'], unitCell['b'], unitCell['c']]

    originalCoords = groupAtoms(struc, 3) # Converts pandas dataframe to a list of lists

    outStruc, strucType = shakeMol(originalCoords, iParams) # Shake the structure
    assert len(outStruc) != 0, "Output structure should have some length"
    assert strucType == 'molecule', "Structure type should be a molecule"