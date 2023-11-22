#EJERCICIO 1. CONTROL 1 (PROBLEMA DE MÁXIMIZACIÓN)
from scipy.optimize import linprog

# Vector de coeficientes de la función objetivo (negativos porque linprog realiza minimización)
Coef = [-1, -1]  # Cambié los coeficientes para reflejar una maximización

# Matriz de Coeficientes para las restricciones 
M_Rest = [[1, 2], [3, 2]]

# Matriz de coeficientes para las desigualdades
M_Coef = [80, 120]

# Defininiendo los Límites para x e y (cantidad mínima de trajes y vestidos)
limites = [(0, None), (0, None)]

# Resolviendo el problema de programación lineal
result = linprog(Coef, A_ub=M_Rest, b_ub=M_Coef, bounds=limites, method='highs')

# Imprimiendo los resultados
print("Cantidad optima de trajes:", round(result.x[0]))
print("Cantidad optima de vestidos:", round(result.x[1]))
print("Ganancia maxima:", -result.fun)  # La función objetivo ahora es positiva
