import re


class validate_document(object):

    def __init__(self):
        super(validate_document, self)
        # Patron para validar la expresion regular"
        self.patron = re.compile("^\\d{8}-\\d$")

    def validate_id_number(self, dui):
        # Variables globales a utilizar
        global residuoVerificador, residuo
        # Se verifica si cumple el patron  para continuar con la validacion
        if self.patron.match(dui):
            # Se obtiene la posicion del digito verificador
            digitoVerificador = int(dui[9])

            # se inicia Variable de posiciones a operar dentro de la cadena
            numero = 10
            # Obtenemos la cadena sin guion
            cadenaDui = dui[0:8]
            # contador
            sum = 0
            # Se itera la cadena operando segun las posiciones
            for indice in range(len(cadenaDui)):
                caracter = cadenaDui[indice]
                numero = numero - 1
                # sumamos  el resultado de multiplicar las posiciones * cada elemento de la cadena o #Dui
                sum = sum + (numero * int(caracter))
                residuo = sum % 10
                # Obtenemos el residuo y lo evaluamos
                if residuo > 0:
                    residuo = residuo - 10
            # Si el residuo es mayor que 0  se realiza la resta de 10
            # luego se realiza la validacion del documento
            if abs(residuo) == digitoVerificador or residuo == 0:
                # Si el residuo es igual al digito verificador o igual a cero
                # El documento se da por validado si no es invalido
                print(" Dui Valido")
                return True
            else:
                print("Dui invalido")
                return False
        else:
            print("Unrecognized pattern")

 validate = validate_document()
 validate.validate_id_number('00322123-4')

# Duis de prueba
# -------------------
# 00322123-4  - Invalido
# 00322123-1  - Valido
