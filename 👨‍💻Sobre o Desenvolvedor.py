import streamlit as st
import base64

st.markdown("""
<style>
.main {
    background-color: #1a222c
}
#mois-s-sthelvyn {
    text-align: center;
    color: white
}
.stMarkdown {
    color: white
}
<style>    
    """, unsafe_allow_html=True)


st.write("## Moisés Sthelvyn")

st.markdown(
    
    """
        Cientista de dados em formação pela Escola Sigmoidal. Já desenvolvi projetos de análises
        exploratórias de dados usando python, projeto de detecção de expressões faciais e sigo
        prosseguindo em enriquecer meu portfólio. Seja bem vindo! Me acompanhe nas redes sociais.
    """
    
)

st.sidebar.info("Me siga no Linkedin para mais projetos e artigos: Moisés Sthelvyn :coffee:")

c1, c2, c3 = st.columns(3)

with c1:
    """
        - Acesse meu [Github](https://github.com/Sthelvyn)
    
    """
with c2:
    """
    
        - Veja meu [Linkedin](https://www.linkedin.com/in/mois%C3%A9s-sthelvyn-aa9791248/)
    
    """
with c3:
    """
    
        - Me siga no [Instagram](https://www.instagram/moisessthelvyn)
    
    """    