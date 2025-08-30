def solicitar_nome():
    pessoas = []
    while True:
        while True:
            nome = input("Escreva seu nome: ").strip()
            if nome != "":
                break
            print("O nome não pode estar vazio. Tente novamente.")

        pessoa = {"Nome": nome}
        pessoas.append(pessoa)

        continuar = input("Deseja adicionar outra pessoa? (s/n): ").strip().lower()
        if continuar != "s":
            break
    return pessoas

def escolher_sala():
    salas = {
        1: "Sala de Reunião 1",
        2: "Sala de Reunião 2",
        3: "Auditório"
    }

    print("\nEscolha uma sala:")
    for numero, nome in salas.items():
        print(f"{numero}. {nome}")

    while True:
        escolha = input("Digite o número da sala desejada: ").strip()
        if escolha.isdigit():
            numero = int(escolha)
            if numero in salas:
                return salas[numero]
        print("Escolha inválida. Tente novamente.")

def validar_data(data_str):
    partes = data_str.split("/")
    if len(partes) != 3:
        return False
    dia, mes, ano = partes
    if not (dia.isdigit() and mes.isdigit() and ano.isdigit()):
        return False
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    if not (1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= ano <= 2100):
        return False
    return True

def validar_horario(horario_str):
    partes = horario_str.split(":")
    if len(partes) != 2:
        return False
    hora, minuto = partes
    if not (hora.isdigit() and minuto.isdigit()):
        return False
    hora = int(hora)
    minuto = int(minuto)
    if 0 <= hora <= 23 and 0 <= minuto <= 59:
        return True
    return False

def reserva_existente(reservas, sala, data, horario):
    for r in reservas:
        if r["sala"] == sala and r["data"] == data and r["horario"] == horario:
            return True
    return False

def ordenar_reservas(reservas):
    def chave_ordenacao(r):
        d = r["data"].split("/")
        h = r["horario"].split(":")
        return (int(d[2]), int(d[1]), int(d[0]), int(h[0]), int(h[1]))
    return sorted(reservas, key=chave_ordenacao)

def solicitar_reservas():
    reservas = []

    print("=== SISTEMA DE RESERVAS ===")
    while True:
        nome = input("\nNome do responsável (ou 'finalizar' para encerrar): ").strip()
        if nome.lower() == "finalizar":
            break
        if nome == "":
            print("O nome não pode estar vazio.")
            continue

        sala = escolher_sala()

        while True:
            data = input("Digite a data da reserva (DD/MM/AAAA): ").strip()
            if validar_data(data):
                break
            print("Data inválida. Tente novamente.")

        while True:
            horario = input("Digite o horário da reserva (HH:MM): ").strip()
            if validar_horario(horario):
                break
            print("Horário inválido. Tente novamente.")

        if reserva_existente(reservas, sala, data, horario):
            print("⚠️ Conflito: Essa sala já está reservada nesse dia e horário!")
        else:
            reservas.append({
                "responsavel": nome,
                "sala": sala,
                "data": data,
                "horario": horario
            })
            print("✅ Reserva confirmada!")

    return reservas

def exibir_reservas(reservas):
    if not reservas:
        print("\nNenhuma reserva foi feita.")
        return

    reservas_ordenadas = ordenar_reservas(reservas)

    print("\n=== RESERVAS CONFIRMADAS ===")
    for r in reservas_ordenadas:
        print(f"{r['data']} {r['horario']} - {r['sala']} - Responsável: {r['responsavel']}")

reservas_confirmadas = solicitar_reservas()
exibir_reservas(reservas_confirmadas)