import openai
import streamlit as st
import os

st.markdown("""
<style>
.main {
    background-color: #1a222c;
    }
#assistente-mark {
    color: white;
}
.stMarkdown {
    color: white;
}
p {
    color: white;
}
</style>""", unsafe_allow_html=True)

response = False

def make_request(question_input: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": f"{question_input},"}
        ]
    )
    return response
openai.api_key = "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"

st.write("# Assistente Mark :brain:")
st.sidebar.success("Insira as informações nos campos correspondentes e clique em Executar.")

st.markdown(
    
     """
        Uma inteligência artificial capaz de auxiliar você com ideias para desenvolvimento
        de projetos de Marketing! Prazer, sou o Mark.
        
    """
    
)

st.markdown(
    """---"""
)

col1, col2 = st.columns(2)

with col1:
    tipo = st.selectbox("Selecione a área do conhecimento", ("Marketing Digital", "Social Media"))
    
with col2:
    nivel = st.selectbox("Selecione o nível", ("Iniciante", 'Intermediário', "Avançado"))

quantidade = st.slider("Quantidade de ideias que você quer", 1, 5, 3)

contexto = st.text_area(
    label="Contexto da aplicação",
    placeholder="Gostaria de um roteiro semanal de postagens para um instagram que fala sobre musculação e vida saudável. Quero dicas e stories, feed e reels", height= 200
)

prompt = f"Olá, seu nome é Mark e é um especialista em marketing digital. Gostaria que você me sugerisse {quantidade} projeto(s) de {tipo}. Meu nível de conhecimento é {nivel}. Considere o contexto {contexto} e me ajude com ideias."

rerun_button = st.button("Executar")

if rerun_button:
    response = make_request(prompt)    
else:
    pass

if response:
    st.write("Response: ")
    st.write(response["choices"] [0] ["message"] ["content"])