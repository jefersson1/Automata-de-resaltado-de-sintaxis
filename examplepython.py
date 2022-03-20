n = int(input('Type a number, and its factorial will be printed: '))

def factorialF(num):
    if num == 1 or num == 0:
        return 1
    else:
        return factorialF(num - 1) * num

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

def prototraductor(codigo):
    codig.clear()
    codigo_abstraido = ""
    '''
    Convención de letras
    a -> palabras reservadas en azul
    r -> " " en rosa
    n -> " " en violeta
    t -> texto normal
    e -> caracter espacio
    '''
    ram=""
    esTextoCmn = True

    for ch in codigo:
        # print(ch,codigo_abstraido,ram)
        if (ord(ch) >= 65 and ord(ch) <= 90) or (ord(ch) >=97 and ord(ch)<=122):
            ram += ch
            esTextoCmn = True
        else:
            if(esTextoCmn==True):
                codig.append(ram)
                if (verfidicc(ram,palResAz)):
                    codigo_abstraido += "a"
                    esTextoCmn  = True
                elif (verfidicc(ram,palResRos)):
                    codigo_abstraido += "r"
                    esTextoCmn  = True
                elif (verfidicc(ram,palResNeg)):
                    codigo_abstraido += "n"
                    esTextoCmn  = True
                else:
                    codigo_abstraido += "t"
                ram = ""
            ram += ch

            if(ch==" "):
                codigo_abstraido += "e"
                codig.append(ram)
            else:
                codig.append(ram)
                codigo_abstraido += "t"
            ram = ""

            esTextoCmn = False
        # print(codigo_abstraido,";",ram,";",esTextoCmn)
    return codigo_abstraido

# if n < 0:
#     raise ValueError('You must enter a non-negative integer")
#
# # sdsdv lafd kjkasdl f dllsld lsdldsj "" sdsdv
#
#
# factorial = 1
# for i in range(2, n + 1):
#     factorial *= i
#
# print(factorial)

"""


"""

# lsldlsdflsld
