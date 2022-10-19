# Lab 8 Davide Attebrant och Vira Oetterli
from linkedQFile import LinkedQ

class Syntaxfel(Exception):
    pass

# Tar emot en queue med bara strings som data och ser om den följer syntax.
def readMolekyl(queue):
    readAtom(queue)
    first_character = queue.peek()
    if first_character == None:
        return
    else:
        readNumber(queue)

# Kommer få första karaktären ofiltrerad, andra karaktären kommer den hantera om ej 0-9.
def readAtom(queue):
    # Kollar först bokstav nummer 1 som måste existera
    first_character = queue.peek()
    # Säkerställer att endast strings matas till readLETTER
    if type(first_character) == str:
        readLETTER(queue)
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet ")  # Om inte en string
    # Kollar nu om det ev. finns en till bokastav. Om ja så kollar vi att den är liten.
    second_character = queue.peek()
    numberlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if second_character not in numberlist and second_character is not None:
        readLetter(queue)

# Denna kan endast ta emot strings. Kollar att de är stora bokstäver.
def readLETTER(queue):
    character = queue.dequeue()
    if character.isupper():
        return
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + character)    # Om inte stor bokstav


# Denna kan endast ta emot strings. Kollar att de är små bokstäver.
def readLetter(queue):
    character = queue.dequeue()
    if character.islower():
        return
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet ")



# Första är garanterat en siffra (fast i sträng format), övriga tecken kan vara strängar.
def readNumber(queue):
    list = []
    # Vi tar ut första värdet för att se om det är 0.
    if not queue.isEmpty():
        list.append(queue.dequeue())
    if list[0] == '0':
        raise Syntaxfel("För litet tal vid radslutet ")
    # Därefter tar vi ut alla övriga värden och ser att de som helhet blir en siffra som är > 1.
    while not queue.isEmpty():
        list.append(queue.dequeue())
    string = ''.join(list)
    try:
        number = int(string)
        if number >= 2:
            return
        else:
            raise Syntaxfel("För litet tal vid radslutet ")
    except:
        raise Syntaxfel("För litet tal vid radslutet ")

# ----------------------------------------Kör Programmet -------------------------------------------------------

# Input är en string. Output en linkedQ med alla karaktärer inlagda.
def storeMolekyl(molekylstring):
    queue = LinkedQ()
    for character in molekylstring:
        queue.enqueue(character)
    return queue



# Input är en string, output är ett meddelande om ifall den följer syntax eller inte.
def kolla_molekyl(molekylstring):
    queue = storeMolekyl(molekylstring)
    try:
        readMolekyl(queue)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
        return str(fel) + str(queue)


# Kör själva programmet
def main():
    string_molekyl = input()
    while string_molekyl != '#':
        print(kolla_molekyl(string_molekyl))
        string_molekyl = input()


'''
def kattis_main():
    stop = False
    while not stop:
        string_molekyl = input("Skriv in en molekyl: ")
        if string_molekyl != '#':
            resultat = kolla_molekyl(string_molekyl)
            print(resultat)
        if string_molekyl == '#':
            stop = True


def kattis_main2():
    string_molekyl = input("Skriv in en molekyl: ")
    list = string_molekyl.splitlines()
    print(list)
    print_list = []
    for i in range(len(list)):
        print(list[i])
        if list[i] == '#':
            break
        else:
            resultat = kolla_molekyl(list[i])
            print_list.append(resultat)
    for i in range(len(print_list)):
        print(print_list[i])'''

'''import unittest
class SyntaxTest(unittest.TestCase):

    def testLETTERletternum(self):
        self.assertEqual(kolla_molekyl("Hb5"), "Formeln är syntaktiskt korrekt")

    def testLETTERletterLETTER(self):
        self.assertEqual(kolla_molekyl("AbD"), "För litet tal vid radslutet ")

    def testletter(self):
        self.assertEqual(kolla_molekyl("b5"), "Saknad stor bokstav vid radslutet b5")

if __name__ == "__main__":
    unittest.main()'''

