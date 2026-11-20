import match

potencia_lampada = float(input("Potência da lãmpada (w): "))
largura = float(input("Largura do cõmoda (m): "))
comprimento = float(input("Comprimento do cõmodo (m): "))


area = largura * comprimento
Potencia_necessaria = area * 3 #3 w poe m²
lampadas = math.ceil(Potencia_necessaria /potencia_lampada)
bocais = math.ceil(area / 3) #1 bocal a cada 3m²

print(f"Área do cõmodo:{area:.2f} m²")
print(f"Potência necessaária:{Potencia_necessaria:.0f} w")
print(f"Lâmpadas de {potencia_lampada:.0f} w necessária:{lampadas}")
print(f"Bocais disponiveis no comodo:{bocais}")

if lampadas > bocais:
    print("Atenção: falatam! Use lâmpadas mais potentes,")
else:
    print("Os bocais são suficientes")