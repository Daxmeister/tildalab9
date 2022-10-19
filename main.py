# Lab 9 Vira Oetterli och Davide Attebrant Sbrzesny

#######################################################################################################################
# BNF-Syntax functioner
#######################################################################################################################

def read_formel():
    '''<formel>::= <mol> \n'''
    pass

def read_molekyl():
    '''<mol>   ::= <group> | <group><mol>'''
    pass

def read_group():
    '''<group> ::= <atom> |<atom><num> | (<mol>) <num>'''
    pass

def read_atom():
    '''<atom>  ::= <LETTER> | <LETTER><letter>'''
    pass
def read_capital_letter():
    '''<LETTER>::= A | B | C | ... | Z'''
    pass

def read_lowercase_letter():
    '''<letter>::= a | b | c | ... | z'''
    pass

def read_number():
    '''<num>   ::= 2 | 3 | 4 | ...'''
    pass

#######################################################################################################################
# Stödfunktioner
#######################################################################################################################

def create_list_of_atoms():
    string = 'H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr ' \
             'Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In ' \
             'Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re ' \
             'Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md ' \
             'No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Fl Lv'
    list_of_atoms = string.split(' ')
    return list_of_atoms









#######################################################################################################################
# Run funktioner
#######################################################################################################################