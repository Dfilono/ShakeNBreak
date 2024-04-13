import TurtleMol as tm
from .shakeCell import shakeMol
from .breakCell import breakMol
from .utils import groupAtoms


def main():
    '''The main loop'''
    # Initizalize input parameters
    iParams = {} # Input Parameters

    # Get input file
    iParams['structureFile'] = input('\nProvide path to input file: ')
    iParams['length'] = input('\nPlease provide the number of atoms per molecue: ')

    struc, unitCell = tm.readStrucFile(iParams['structureFile']) # Converts pdb or xyz files in pandas dataframe

    if unitCell:
        iParams['unitCell'] = [unitCell['a'], unitCell['b'], unitCell['c']]

    originalCoords = groupAtoms(struc, iParams['length']) # Converts pandas dataframe to a list of lists

    # Choose whether or Shake or Break the system
    iParams['mode'] = input('\nWhat would you like to do? (Shake, Break, ShakeNBreak, BreakNShake): ') 
    
    # Run appropriate method for defined mode
    if iParams['mode'].lower() == 'shake':
        iParams['magnitude'] = input('\nHow much would you like molecules to move? (Units in Angstroms): ')
        outStruc, strucType = shakeMol(originalCoords, iParams) # Shake the structure

    elif iParams['mode'].lower() == 'break':
        iParams['remove'] = input('\nWhat percent of molecules should be removed? (i.e. 10): ')
        outStruc, strucType = breakMol(originalCoords, iParams) # Remove molecules from the structre

    elif iParams['mode'].lower() == 'shakenbreak':
        iParams['magnitude'] = input('\nHow much would you like molecules to move? (Units in Angstroms): ')
        midStruc, strucType = shakeMol(originalCoords, iParams) # Shake the structure
        iParams['remove'] = input('\nWhat percent of molecules should be removed? (i.e. 10): ')
        outStruc, strucType = breakMol(midStruc, iParams) # Remove molecules from the structre

    elif iParams['mode'].lower() == 'breaknshake':
        iParams['remove'] = input('\nWhat percent of molecules should be removed? (i.e. 10): ')
        midStruc, strucType = breakMol(originalCoords, iParams) # Remove molecules from the structre
        iParams['magnitude'] = input('\nHow much would you like molecules to move? (Units in Angstroms): ')
        outStruc, strucType = shakeMol(midStruc, iParams) # Shake the structure
        
    iParams['output'] = input('Where would you like to save your file?: ') # provide path for outputfile to be written
    if unitCell:
        tm.writeOutput(outStruc, iParams['output'], strucType, unitCell)
    else:
        tm.writeOutput(outStruc, iParams['output'], strucType)

if __name__ == "__main__":
    main()