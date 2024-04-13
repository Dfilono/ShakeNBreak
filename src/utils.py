'''Extra helper functions'''

def groupAtoms(struc, n):
    '''Convert dataframe to list of points'''
    atomBase = struc['Atom'].values.tolist()
    xBase = struc['X'].values.tolist()
    yBase = struc['Y'].values.tolist()
    zBase = struc['Z'].values.tolist()

    if 'Residue' not in struc.columns:

        # combine individual list into a list of lists
        atoms = [[atomBase[i], xBase[i], yBase[i],zBase[i]] for i in range(len(atomBase))]

        # Group atoms into sublists of size n
        groupedAtoms = [atoms[i: i + n] for i in range(0, len(atoms), n)]

        return groupedAtoms
    
    res = struc['Residue'].values.tolist()

    # combine individual list into a list of lists
    atoms = [[atomBase[i], xBase[i], yBase[i],zBase[i], res[i]] for i in range(len(atomBase))]
    
    # Group atoms into sublists of size n
    groupedAtoms = [atoms[i: i + n] for i in range(0, len(atoms), n)]
    return groupedAtoms
