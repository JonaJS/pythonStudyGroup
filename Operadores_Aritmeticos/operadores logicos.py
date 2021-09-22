# OPERADORES LOGICOS

"""
* Permite constryir expresiones logicas obteniendo resultados booleanos

* TIPOS :
 and CONJUNCION
 or  DISYUNCION
 not NEGACION
"""

#************** EJECUCION ********************

a = 10
b = 12
c = 13

funcion = ((a > b) or (a < c)) and ((a == c) or (a >= b))
 #  false    true         false     false
# ( true  )   and                 (false)
# false

print(not funcion)
print(type(funcion))

""" Prioridad de los operadores:  (), **, * / mod not, + - and
 >< == >= <= != or """

