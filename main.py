import streamlit as st
import pandas as pd

# Criar um DataFrame para armazenar as reservas
reservas = pd.DataFrame(columns=["Nome", "Data", "Hora", "Número de Pessoas"])

# Título do aplicativo
st.title("Reserva de Mesa em Restaurante")


def main():
        
    # Adicionar uma opção para fazer uma nova reserva
    if st.button("Fazer Nova Reserva"):
        # Formulário para entrada de informações da reserva
        nome = st.text_input("Nome")
        data = st.date_input("Data")
        hora = st.time_input("Hora")
        num_pessoas = st.number_input("Número de Pessoas", min_value=1, max_value=20, value=1)

        # Adicionar a reserva ao DataFrame
        if st.button("Confirmar Reserva"):
            reservas = reservas.append({"Nome": nome, "Data": data, "Hora": hora, "Número de Pessoas": num_pessoas}, ignore_index=True)
            st.success("Reserva confirmada com sucesso!")

            # Mostrar a lista de reservas existentes
            st.subheader("Reservas Existente:")
            st.write(reservas)

    # Adicionar a capacidade de exportar as reservas para um arquivo CSV
    if st.button("Exportar Reservas"):
        reservas.to_csv("reservas.csv", index=False)
        st.success("Reservas exportadas para reservas.csv")

    # Adicionar a capacidade de limpar todas as reservas
    if st.button("Limpar Todas as Reservas"):
        reservas = pd.DataFrame(columns=["Nome", "Data", "Hora", "Número de Pessoas"])
        st.success("Todas as reservas foram removidas!")

# Rodar o aplicativo
if __name__ == "__main__":
    main()
