from peptide  import Peptide
from modifications import Modifications
from elements import Formulas

mods = Modifications()
phospho    = mods.mods_unimods[21]
oxi        = mods.mods_TPPcode['M[147]'];
cys        = mods.mods_TPPcode['C[160]'];
nTMT       = mods.mods_TPPcode['n[230]'];
TMT        = mods.mods_TPPcode['K[357]'];

massNH3 = Formulas.mass(Formulas.NH3) #massN + 3 * massH
massH2O = Formulas.mass(Formulas.H2O) #(massH *2 + massO) 

p1  = Peptide('CKDALA',modifications={1: cys})
p2  = Peptide('CKDALA',modifications={1: cys, 0: nTMT, 2:TMT})

for pep in [ p1, p2 ]: 

#    annot , ion_masses = pep.all_ions(ionseries = ['y','b'], 
#                                      frg_z_list = [1,2], 
#                                      fragmentlossgains = [0, ], 
#                                      mass_limits = [100,3000], 
#                                      label = '')
#    for a in annot: 
#        print a


    print "PEPTIDE:", pep.getSequenceWithMods("TPP"), "\tpreMz:", pep.getMZ(2)      #CHARGE=2

    for v in range(1, len(pep.sequence)):

        print [v, pep.sequence[v], 
                 pep.getMZfragment('b', v, 1),     #b ion 1 charge
                 pep.getMZfragment('b', v, 2),     #b ion 2 charge
                 pep.getMZfragment('b', v, 1, fragmentlossgain=-massH2O),     #b water loss
                 pep.getMZfragment('b', v, 1, fragmentlossgain=-massNH3),    #b amonia loss
                 pep.getMZfragment('y', v, 1),     #y ion 1 charge
                 pep.getMZfragment('y', v, 2),     #y ion 2 charge
                 pep.getMZfragment('y', v, 1, fragmentlossgain=-massH2O),    #y water loss
                 pep.getMZfragment('y', v, 1, fragmentlossgain=-massNH3)     #y amonia loss
              ]
