def inverter_fila(fila):
    return fila[::-1]


# Uso
if __name__ == "__main__":
    # Exemplo fila de pacientes
    fila_pacientes = ["Paciente 1", "Paciente 2", "Paciente 3", "Paciente 4"]

    print("Fila original:", fila_pacientes)
    fila_invertida = inverter_fila(fila_pacientes)
    print("Fila invertida:", fila_invertida)
