import numpy as np

# Implementação dos métodos de resolução de equações não lineares

def bissecao(f, a, b, tol, max_iter):
    iterations = []
    values = []
    if np.sign(f(a)) * np.sign(f(b)) >= 0:
        raise ValueError("A função deve mudar de sinal no intervalo.")
    
    for i in range(max_iter):
        c = (a + b) / 2
        iterations.append(i)
        values.append(c)
        
        if abs(f(c)) < tol:
            break
        
        if np.sign(f(c)) * np.sign(f(a)) < 0:
            b = c
        else:
            a = c
    
    return iterations, values

def falsa_posicao(f, a, b, tol, max_iter):
    iterations = []
    values = []
    if np.sign(f(a)) * np.sign(f(b)) >= 0:
        raise ValueError("A função deve mudar de sinal no intervalo.")
    
    for i in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        iterations.append(i)
        values.append(c)
        
        if abs(f(c)) < tol:
            break
        
        if np.sign(f(c)) * np.sign(f(a)) < 0:
            b = c
        else:
            a = c
    
    return iterations, values

def secante(f, x0, x1, tol, max_iter):
    iterations = []
    values = []
    
    for i in range(max_iter):
        if abs(f(x1)) < tol:
            break
        
        x_next = x1 - f(x1) * ((x1 - x0) / (f(x1) - f(x0)))
        iterations.append(i)
        values.append(x_next)
        
        x0 = x1
        x1 = x_next
    
    return iterations, values

def newton(f, df, x0, tol, max_iter):
    iterations = []
    values = []
    
    for i in range(max_iter):
        if abs(f(x0)) < tol:
            break
        
        x_next = x0 - f(x0) / df(x0)
        iterations.append(i)
        values.append(x_next)
        
        x0 = x_next
    
    return iterations, values

def iteracao_linear_modificada(g, x0, tol, max_iter):
    iterations = []
    values = []
    
    for i in range(max_iter):
        if abs(g(x0) - x0) < tol:
            break
        
        iterations.append(i)
        values.append(g(x0))
        
        x0 = g(x0)
    
    return iterations, values

# Implementação de funções f(x) e suas derivadas, caso necessário
def funcao(x):
    return x ** 3 - 6 * x ** 2 + 11 * x - 6

def derivada_funcao(x):
    return 3 * x ** 2 - 12 * x + 11

def g(x):
    return (x ** 3 - 6 * x ** 2 + 11 * x) / 6  # Função para a iteração linear modificada

# Definição dos parâmetros do intervalo [a, b], tolerância e número máximo de iterações
a = 0
b = 2
tolerancia = 1e-5
max_iteracoes = 1000

# Execução dos métodos
resultados = {
    "bissecao": bissecao(funcao, a, b, tolerancia, max_iteracoes),
    "falsa_posicao": falsa_posicao(funcao, a, b, tolerancia, max_iteracoes),
    "secante": secante(funcao, a, b, tolerancia, max_iteracoes),
    "newton": newton(funcao, derivada_funcao, a, tolerancia, max_iteracoes),
    "iteracao_linear_modificada": iteracao_linear_modificada(g, a, tolerancia, max_iteracoes)
}

# Salvar resultados em arquivo
with open("resultados.txt", 'w') as file:
    file.write("Iterações\tBisseção\tFalsa Posição\tSecante\tNewton\tIteração Linear Modificada\n")
    for i in range(max_iteracoes):
        file.write(f"{i}\t")
        for _, values in resultados.items():
            if i < len(values[0]):
                file.write(f"{values[1][i]}\t")
            else:
                file.write("\t")
        file.write("\n")

print("Resultados salvos no arquivo 'resultados.txt'")