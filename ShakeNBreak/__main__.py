'''The main file for ShakeNBreak'''

import TurtleMol as tm
from .shakeCell import shakeMol
from .breakCell import breakMol
from .utils import groupAtoms


def main():
    '''The main loop'''
    # Initizalize input parameters
    iParams = {} # Input Parameters

    # Get input file
    print('\nProvide path to input file: ')
    iParams['structureFile'] = input()
    print('\nPlease provide the number of atoms per molecue: ')
    iParams['length'] = input()

    struc, unitCell = tm.readStrucFile(
        iParams['structureFile']) # Converts pdb or xyz files in pandas dataframe

    if unitCell:
        iParams['unitCell'] = [unitCell['a'], unitCell['b'], unitCell['c']]

    originalCoords = groupAtoms(
        struc, iParams['length']) # Converts pandas dataframe to a list of lists

    # Choose whether or Shake or Break the system
    print('\nWhat would you like to do? (Shake, Break, ShakeNBreak, BreakNShake): ')
    iParams['mode'] = input()

    # Run appropriate method for defined mode
    if iParams['mode'].lower() == 'shake':
        print('\nHow much would you like molecules to move? (Units in Angstroms): ')
        iParams['magnitude'] = input()
        outStruc, strucType = shakeMol(originalCoords, iParams) # Shake the structure

    elif iParams['mode'].lower() == 'break':
        print('\nWhat percent of molecules should be removed? (i.e. 10): ')
        iParams['remove'] = input()
        outStruc, strucType = breakMol(originalCoords, iParams) # Remove molecules from the structre

    elif iParams['mode'].lower() == 'shakenbreak':
        print('\nHow much would you like molecules to move? (Units in Angstroms): ')
        iParams['magnitude'] = input()
        midStruc, strucType = shakeMol(originalCoords, iParams) # Shake the structure
        print('\nWhat percent of molecules should be removed? (i.e. 10): ')
        iParams['remove'] = input()
        outStruc, strucType = breakMol(midStruc, iParams) # Remove molecules from the structre

    elif iParams['mode'].lower() == 'breaknshake':
        print('\nWhat percent of molecules should be removed? (i.e. 10): ')
        iParams['remove'] = input()
        midStruc, strucType = breakMol(originalCoords, iParams) # Remove molecules from the structre
        print('\nHow much would you like molecules to move? (Units in Angstroms): ')
        iParams['magnitude'] = input()
        outStruc, strucType = shakeMol(midStruc, iParams) # Shake the structure

    print('Where would you like to save your file?: ')
    iParams['output'] = input() # provide path for outputfile to be written

    if unitCell:
        tm.writeOutput(outStruc, iParams['output'], strucType, unitCell)
    else:
        tm.writeOutput(outStruc, iParams['output'], strucType)

if __name__ == "__main__":
    main()
