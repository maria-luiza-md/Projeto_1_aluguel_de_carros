import streamlit as st

#----------------------------SIDEBAR

st.sidebar.title("Multiuso(carros)")

carros = ["jeep" ,"Dodge ram","BMW", "Mustang"]
carro = st.sidebar.selectbox("escolha seu carros:" , carros)

#-----------------------------BODY

st.title("Multiuso(carros)")
st.image(f"{carro}.png")
st.write(f"voce alugou o {carro}")

dias = st.text_input(f"por quantos dias vcoe alugou o {carro}? ")
km = st.text_input(f"quntos km voce rodou com o {carro}?")


if carro == "BMW":
    diaria = 600

elif carro == "jeep":
    diaria = 600

elif carro == "Dodge ram":
    diaria = 1.500

elif carro == "Mustang":
    diario = 2000.00

if st.button("Calcular"):
    dias = int(dias)
    km = int (km)

    total = (dias * diaria) + (km * 0.15 )

    st.Waring(f"o todal do aluguel a se pegar e R${total}.SS")

