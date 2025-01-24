import streamlit as st
import pandas as pd
from src.utils.api_utils import weak_supervision_label


dict_credibility_signals = {
    'Evidence' : 'Does the article present any supporting evidence or arguments to substantiate its claims?',
    'Bias' : 'Does the article contain explicit or implicit biases?',
    'Inference' : 'Does the article make claims about correlation and causation?',
}

models = ["google:gemini-1.5-flash-002"]

# Título do aplicativo
st.title("Analisador de Credibilidade de Notícias")

# Caixa de texto para o usuário inserir a notícia
noticia = st.text_area("Digite ou cole a notícia aqui:")

origem = st.text_input("Digite de onde essa notícia foi retirada:")

articles = pd.DataFrame({'article_content': [noticia], 'source': [origem]})

# Botão para submeter
if st.button("Analisar Credibilidade"):
    if noticia.strip():  # Verifica se a notícia não está vazia
        # Inicia a análise
        with st.spinner('Analisando a credibilidade da notícia...'):
            # Chama a função de análise
            resultados = weak_supervision_label(articles, models, dict_credibility_signals, temperature=0.1)

        # Exibe os resultados com ticker
        st.success("Análise concluída!")
        st.dataframe(resultados)
        # for resultado in resultados:
        #     if resultado['resultado'] == True:
        #         status = "✅ Positivo"
        #     elif resultado['resultado'] == False:
        #         status = "❌ Negativo"
        #     else:  # Caso seja "Abstain"
        #         status = "⚪ Abstain (Sem Conclusão)"

        #     with st.expander(f"**{resultado['sinal']}**: {status}"):
        #         st.write(resultado["explicacao"])


    else:
        st.error("Por favor, insira uma notícia antes de enviar!")