import random

def generate_cpf():
    # Gera os 9 primeiros dígitos do CPF aleatoriamente
    cpf = [random.randint(0, 9) for _ in range(9)]

    # Calcula o primeiro dígito verificador do CPF
    sum1 = sum(x * y for x, y in zip(cpf, range(10, 1, -1)))
    digit1 = (sum1 * 10) % 11
    if digit1 == 10:
        digit1 = 0
    cpf.append(digit1)

    # Calcula o segundo dígito verificador do CPF
    sum2 = sum(x * y for x, y in zip(cpf, range(11, 1, -1)))
    digit2 = (sum2 * 10) % 11
    if digit2 == 10:
        digit2 = 0
    cpf.append(digit2)

    return ''.join(str(d) for d in cpf)

# Gerar 10 CPFs válidos simulados
if __name__ == "__main__":
    for _ in range(2):
        cpf = generate_cpf()
        print(cpf)
