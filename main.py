# Lab 9 Vira Oetterli och Davide Attebrant Sbrzesny

from linkedQFile import LinkedQ


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

def enqueue_formel(formel_string):
    queue = LinkedQ()
    for character in formel_string:
        if character != '\n' and character != ' ':
            queue.enqueue(character)
    return queue


#######################################################################################################################
# BNF-Syntax functioner
#######################################################################################################################
class Syntaxfel(Exception):
    pass

def read_formel(queue):
    '''<formel>::= <mol> \n'''
    read_molekyl(queue, False)

def read_molekyl(queue, back_from_parenthesis):
    '''<mol>   ::= <group> | <group><mol>'''
    read_group(queue)
    if not queue.isEmpty():
        if queue.peek() == ")":
            return
        read_molekyl(queue, False)
    '''
    if back_from_parenthesis:
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if queue.peek() not in numbers:
            raise Syntaxfel("Saknad siffra vid radslutet ")
        read_number(queue, False)
        return
    if queue.isEmpty():
        return
    read_molekyl(queue, False)'''

# Grupp. Får börja med atom eller start-parentes.
# Är gruppstart inte en bokstav eller "(" ska vi få meddelande fel gruppstart.
# Annars ska vi antingen läsa in atom + nummer
# Eller ropa på molekyl igen och sen läsa nummer.
def read_group(queue):
    '''<group> ::= <atom> |<atom><num> | (<mol>) <num>'''
    first_character = queue.peek()
    acceptable_groupstart_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz("
    if first_character not in acceptable_groupstart_characters:
        raise Syntaxfel("Felaktig gruppstart vid radslutet ")

    if first_character != "(":
        '''<atom> | <atom><num>'''
        read_atom(queue)
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if queue.peek() in numbers:
            read_number(queue)

    else:
        queue.dequeue() # Ta bort startparentes
        read_molekyl(queue, False)
        if queue.peek() != ")":
            raise Syntaxfel("Saknad högerparentes vid radslutet ")
        queue.dequeue() # Tar bort slutparentes
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if queue.peek() not in numbers:
            raise Syntaxfel ("Saknad siffra vid radslutet ")
        read_number(queue)




    '''if first_character == "(":
        (<mol>) <num>
        queue.dequeue() # Tar bort startparentesen
        new_string = ""
        while queue.peek() != ")":
            new_string += queue.dequeue()
        if queue.peek() != ")":
            raise Syntaxfel("Saknad högerparentes vid radslutet ")
        new_queue = enqueue_formel(new_string)
        read_molekyl(new_queue)

        # Kollar att det kommer en siffta efter och läser den.
        next_character = queue.peek()
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if next_character not in numbers:
            raise Syntaxfel("De angav ingen siffra efter parentesslut") # Eget felmeddelande aftersom detta scenarion ej specificerats
        else:
            read_number(queue)'''




# Kollar om stor bokstav, ger fel annars. Kollar om nästa är en liten bokstav och kommer isåfall tugga upp den också.
# Jämför dessa två med bekanta atomer. OBS att den inte kollar vidare på queue. Läser max in två tecken.
# Klarar inte att få None skickat till sig.
def read_atom(queue):
    '''<atom>  ::= <LETTER> | <LETTER><letter>'''
    # Läser in stora och små bokstäver

    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Kollar att första bokstaven är stor, annars fel
    next_character = queue.peek()
    if next_character not in capital_letters:
        raise Syntaxfel("Saknad stor bokstav vid radslutet ")

    #Läser första bokstaven
    read_capital_letter(queue)

    # Kollar på nästa tecken, är det en liten bokstav blir den inläst.
    next_next_character = queue.peek()
    atom = next_character
    if next_next_character != None and next_next_character in lowercase_letters:
        atom = next_character + next_next_character
        read_lowercase_letter(queue)

    # Jämför vår atom av en eller två bokstäver med listan.
    accepted_atoms_list = create_list_of_atoms()
    if atom in accepted_atoms_list:
        return
    else:
        raise Syntaxfel("Okänd atom vid radslutet ")



# Kan få vad som helst, ser om stor bokstav
def read_capital_letter(queue):
    '''<LETTER>::= A | B | C | ... | Z'''
    capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    character = queue.dequeue()
    if character in capital_letters:
        return
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + character)

# Kan få vad som helst, ser om det är liten bokstav.
def read_lowercase_letter(queue):
    '''<letter>::= a | b | c | ... | z'''
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    character = queue.dequeue()
    if character in lowercase_letters:
        return
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet ")


"""def read_number(queue):
    '''<num>   ::= 2 | 3 | 4 | ...'''
    acceptable_first_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    number_string = queue.dequeue()
    if number_string in acceptable_first_numbers:
        return
    else:
        raise Syntaxfel("För litet tal vid radslutet ")

    while queue.peek() in acceptable_first_numbers or queue.peek() == "0":
        number_string == number_string + queue.dequeue()
        try:
            number = int(number_string)
            if number >= 2:
                pass
            else:
                raise Syntaxfel("För litet tal vid radslutet ")
        except:
            raise Syntaxfel("För litet tal vid radslutet ")"""


def read_number(queue):
    '''<num>   ::= 2 | 3 | 4 | ...'''
    number_string = queue.dequeue()
    if number_string == "0":
        raise Syntaxfel("För litet tal vid radslutet ")
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if number_string == "1":
        next_numberstring = queue.peek()
        if next_numberstring in numbers:
            pass
        else:
            raise Syntaxfel("För litet tal vid radslutet ")
    while queue.peek() in numbers:  # Alla siffror på rad dequeueas.
        queue.dequeue()

#######################################################################################################################
# Run funktioner
#######################################################################################################################
# Input är en string, output är ett meddelande om ifall den följer syntax eller inte.
def kolla_molekyl(molekylstring):
    queue = enqueue_formel(molekylstring)
    try:
        read_formel(queue)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
        return str(fel) + str(queue)

# Kör själva programmet
def main():
    string_molekyl = input()
    while string_molekyl != '#':
        print(kolla_molekyl(string_molekyl))
        string_molekyl = input()

main()

exit()
sample_string = ""
sample_queue = enqueue_formel(sample_string)
read_molekyl(sample_queue)



