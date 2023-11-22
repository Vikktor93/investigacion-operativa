from scipy.optimize import linprog

# Vector de coeficientes de la función objetivo 
Coef_Obj = [-0.58, -0.9]

# Matriz de Coeficientes para las restricciones 
M_Rest = [[0.5, 0.8], [1, 1]] #Cada fila es una restricción, y cada columna una variable (Manzanas Rojas y Manzanas Verdes)

# Matriz de coeficientes para las desigualdades
M_Coef = [500, 700]

# Defininiendo los Límites para x e y 
limiteX = (0, None) # Las manzanas rojas no pueden ser negativas y no hay límite superior
limiteY = (0, None) # Las manzanas verdes no pueden ser negativas y no hay límite superior

# Resolviendo el problema de programación lineal (A_ub: es la matriz de coeficientes para las restricciones, b_ub es la matriz de coeficientes para las desigualdades)
result = linprog(Coef_Obj, A_ub=M_Rest, b_ub=M_Coef, bounds=[limiteX, limiteY], method='highs') #highs es por Solver HiGHS

# Solución
manzanas_verdes = result.x[0] #result.x[0] es la solución para la variable 0 (manzanas verdes)
manzanas_rojas = result.x[1] #result.x[1] es la solución para la variable 1 (manzanas rojas)
beneficio_maximo = -result.fun #result.fun es el valor de la función objetivo, es negativo porque se está maximizando

# Imprimir resultados
print("La cantidad óptima de manzanas verdes (kg):", manzanas_verdes)
print("La cantidad óptima de manzanas rojas (kg):", manzanas_rojas)
print("El beneficio máximo (UM):", beneficio_maximo)

