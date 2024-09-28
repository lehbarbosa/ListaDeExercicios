print("\033[33m ===== Média das Notas =====\033[0m")
note = float(input("Digite a primeira nota: "))
note1 = float(input("Digite a segunda nota: "))
note2 = float(input("Digite a terceira nota: "))
note3 = float(input("Digite a quarta nota: "))

average = (note + note1 + note2 + note3) / 4
print(f"A média do aluno é {average:.2f}")


