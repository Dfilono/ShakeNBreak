'''Functions to shake molecules'''

import random
import numpy as np
import TurtleMol as tm

def shakeMol(struc, iParams):
    '''Shakes molecules based on defined parameters'''
    radii = tm.setAtomicRadius('AtomicRadius') # Get atomic radii
    translatedCoords = [] # Initialize list of translated coordinates

    # Initialize KD-Tree for collision checking
    kdTree, indexToAtom = tm.buildKDTreeMapping(translatedCoords, radii)

    for mol in struc:
        atomNames = [atom[0] for atom in mol]
        atomInfo = [
            atom[4:] if len(atom) > 4 else [] for atom in mol
            ] # Get bonding information from pdb files
        points = np.array([atom[1:4] for atom in mol], dtype=np.float64)

        # Perform random translation for each molecules
        dx = random.uniform(-iParams['magnitude'], iParams['magnitude'])
        dy = random.uniform(-iParams['magnitude'], iParams['magnitude'])
        dz = random.uniform(-iParams['magnitude'], iParams['magnitude'])

        # Apply the translation to each point
        newPoints = points + np.array([dx, dy, dz])

        # Recreate the molecule with new coordinates and original information
        newMol = [
            (atomNames[i], newPoints[i][0], newPoints[i][1], newPoints[i][2],
             atomInfo[i]) for i in range(len(points))
            ]

        # Check if new position collides with other molecules
        if kdTree is None or not tm.isOverlapMoleculeKDTree(
            newMol, kdTree, indexToAtom, radii, tol=1):
            translatedCoords.append(newMol)

    return translatedCoords, 'molecule'
