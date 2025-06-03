
import streamlit as st
import qrcode
from PIL import Image
import io

st.set_page_config(page_title="Fe & Bia ❤️", page_icon="❤️", layout="centered")

# CSS para centralizar tudo
st.markdown(
    """
    <style>
    .main {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .block-container {
        max-width: 1000px;
        padding-top: 3rem;
        padding-bottom: 3rem;
        margin: auto;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def gerar_qrcode(link):
    qr = qrcode.make(link)
    buf = io.BytesIO()
    qr.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

# Perguntas do quiz
perguntas = [
    {"pergunta": "Onde foi nosso primeiro encontro?", "opcoes": ["Cinema", "Praça", "Restaurante", "Parque"], "resposta": "Restaurante"},
    {"pergunta": "Qual nossa data de aniversário de namoro?", "opcoes": ["01/02", "14/03", "20/05", "10/10"], "resposta": "20/05"},
    {"pergunta": "Qual é meu prato favorito?", "opcoes": ["Pizza", "Lasanha", "Sushi", "Hamburguer"], "resposta": "Sushi"},
    {"pergunta": "Para qual lugar sonhamos viajar?", "opcoes": ["Paris", "Maldivas", "Gramado", "Nova York"], "resposta": "Maldivas"},
    {"pergunta": "Qual foi nosso primeiro filme juntos?", "opcoes": ["Titanic", "Vingadores", "Up Altas Aventuras", "Avatar"], "resposta": "Vingadores"},
    {"pergunta": "Qual apelido eu te chamo?", "opcoes": ["Amor", "Vida", "Bebê", "Mozão"], "resposta": "Vida"},
    {"pergunta": "Qual presente mais te surpreendeu?", "opcoes": ["Flores", "Caixa surpresa", "Viagem", "Jantar"], "resposta": "Caixa surpresa"},
    {"pergunta": "Qual cor mais representa nosso amor?", "opcoes": ["Vermelho", "Rosa", "Branco", "Preto"], "resposta": "Vermelho"},
    {"pergunta": "Nos conhecemos em qual ano?", "opcoes": ["2018", "2019", "2020", "2021"], "resposta": "2020"},
    {"pergunta": "Se fossemos um animal juntos, seríamos...", "opcoes": ["Pinguins", "Leões", "Cachorros", "Gatinhos"], "resposta": "Pinguins"},
]

if 'page' not in st.session_state:
    st.session_state.page = 0
if 'respostas' not in st.session_state:
    st.session_state.respostas = []

def next_page():
    st.session_state.page += 1

st.markdown(
    "<h1 style='text-align: center; color: #FF4B4B;'>Fe & Bia ❤️</h1>",
    unsafe_allow_html=True,
)

if st.session_state.page == 0:
    st.subheader("Seja bem-vinda ao nosso quiz do amor!")
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.image("assets/coracoes.gif", width=300)
    st.write("Clique no botão abaixo para começar.")
    if st.button("Começar"):
        next_page()

elif 1 <= st.session_state.page <= 10:
    idx = st.session_state.page - 1
    q = perguntas[idx]
    st.subheader(f"Pergunta {idx + 1} de 10")
    st.write(q["pergunta"])
    opcao = st.radio("Escolha uma opção:", q["opcoes"], key=idx)
    if st.button("Próxima"):
        st.session_state.respostas.append(opcao)
        next_page()

elif st.session_state.page == 11:
    st.subheader("✨ Resultado ✨")
    acertos = sum([1 for i, q in enumerate(perguntas) if st.session_state.respostas[i] == q["resposta"]])
    st.write(f"Você acertou {acertos} de 10 perguntas! ❤️")
    if st.button("Ver Surpresa"):
        next_page()

elif st.session_state.page == 12:
    st.subheader("📸 Uma lembrança nossa")
    st.image("assets/foto_nossa.JPG", caption="Nós ❤️", width=300)
    st.write("“Você é a razão dos meus sorrisos, dos meus sonhos e da minha felicidade. Te amo mais do que as palavras podem expressar.”")
    if st.button("Próxima"):
        next_page()

elif st.session_state.page == 13:
    st.subheader("🎁 Tem mais vindo aí...")
    st.write("Prepare-se para mais uma surpresa que está chegando no final!")
    if st.button("Ir para o final"):
        next_page()

elif st.session_state.page == 14:
    st.subheader("🎶 Nossa música")
    qr_code = gerar_qrcode("https://youtu.be/FsfrC0nwFIU?si=0VJbqK7as9YzfPhx")
    st.image(qr_code, caption="Escaneie para ouvir nossa música ❤️", width=250)
    st.markdown("[Ou clique aqui para ouvir](https://youtu.be/FsfrC0nwFIU?si=0VJbqK7as9YzfPhx)")
