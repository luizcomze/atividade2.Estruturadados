from collections import deque

# Passo 1: Inserir números [1, 2, 3, 4, 5] na lista com 5 células
lista = [1, 2, 3, 4, 5]

# Passo 2: Remover da lista e inserir na pilha com 5 células
pilha = []
for _ in range(5):
    pilha.append(lista.pop(0))

# Passo 3: Remover da pilha e inserir na fila com 10 células
fila = deque()
while pilha:
    fila.append(pilha.pop())

# Passo 4: Inserir números [6, 7, 8, 9, 10] na lista
lista.extend([6, 7, 8, 9, 10])

# Passo 5: Repetir passos 2 e 3
for _ in range(2):
    pilha.clear()
    for _ in range(5):
        pilha.append(lista.pop(0))
    
    while pilha:
        fila.append(pilha.pop())

# Passo 6: Exibir todos os números que foram inseridos na fila
print("Números na fila:")
while fila:
    print(fila.popleft())
