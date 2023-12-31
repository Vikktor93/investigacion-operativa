#EJERCICIO 2. CONTROL 2 (PROBLEMA DE MÁXIMIZACIÓN)
from scipy.optimize import linprog

# Coeficientes de la función objetivo (negativos porque linprog realiza minimización)
c = [-7, -4, -3]  # Utilidades por cerveza rubia, negra y de baja graduación respectivamente

# Coeficientes de las restricciones (matriz A)
A = [
    [1, 2, 2],   # Malta para cerveza rubia
    [2, 1, 2]    # Levadura para cerveza negra
]

# Límites superiores de las restricciones (cantidad máxima de materia prima diaria)
b_ub = [30, 45]

# Límites inferiores de las variables (cantidad mínima de cerveza de cada tipo)
bounds = [(0, None), (0, None), (0, None)]

# Resolviendo el problema de programación lineal
result = linprog(c, A_ub=A, b_ub=b_ub, bounds=bounds, method='highs')

# Imprimiendo los resultados
print("Cantidad óptima de cerveza rubia:", round(result.x[0]))
print("Cantidad óptima de cerveza negra:", round(result.x[1]))
print("Cantidad óptima de cerveza de baja graduación:", round(result.x[2]))
print("Beneficio máximo:", -result.fun)  # La función objetivo ahora es positiva
