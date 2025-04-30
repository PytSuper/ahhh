def convbinario(num):
    pila = []
    
    if num == 0:
        print("0")
        return
    while num > 0:
        residuo = num % 2
        pila.append(residuo)
        num = num // 2
        
    while pila:
        print(pila.pop(), end="")
        
    print()