def example_1() -> None:
    print("Atividade 01")
    name = input("Digite seu nome: ")
    count_name = len(name)

    print(f"{name}, seu nome contém {count_name} caracteres")


def example_2() -> None:
    print("Atividade 02")
    values_count = int(input("Insira quantos valores você deseja somar: "))

    sum_values = 0
    for value in range(values_count):
        value = int(input(f"Insira o valor {value +1}: "))
        sum_values += value

    print(f"A soma dos valores é {sum_values}")


def challenge(constant_bonus: float) -> None:
    print("Desafio")
    # Solicite ao usuário que defina o seu nome
    name = str(input("Qual o seu nome: "))
    # Solicite que o usuário digite o valor do seu salário
    salary = float(input(f"Qual o valor do seu salário {name}? "))
    # Solicite o valor do bônus recebido
    bonus = float(input(f"Quanto você recebe de bônus {name}: "))
    # Calcule o valor do bônus final
    final_bonus = float(salary * bonus + constant_bonus)
    # Imprima uma mensagem personalizada
    print(f"{name}, você irá receber {final_bonus} em 2024")


if __name__ == "__main__":
    example_1()
    example_2()
    challenge(1000)
