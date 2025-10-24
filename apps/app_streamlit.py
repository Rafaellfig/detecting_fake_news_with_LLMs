import streamlit as st
import pandas as pd
from src.utils.api_utils import process_credibility_signal
import concurrent.futures

def add_result_callback(future):
    try:
        result = future.result()
        st.session_state.results.append(result)
    except Exception as e:
        st.session_state.results.append({"error": str(e)})

st.title("Analisador de Credibilidade de Notícias")

# Entradas do usuário
noticia = st.text_area("Digite ou cole a notícia aqui:")
origem = st.text_input("Digite de onde essa notícia foi retirada:")

# Exemplo de dicionário de sinais de credibilidade e lista de modelos
dict_credibility_signals = {
    'Evidence': 'Does the article present any supporting evidence or arguments to substantiate its claims for {organization_name}?',
    'Bias': 'Does the article contain explicit or implicit biases in {organization_name}?',
    'Inference': 'Does the article make claims about correlation and causation in {organization_name}?'
}
models = ["deepseek:deepseek-chat"]

# Ao clicar no botão, inicia o processamento e exibe os resultados conforme eles chegam
if st.button("Analisar Credibilidade"):
    if noticia.strip():
        # Cria o DataFrame de artigo
        articles = pd.DataFrame({'article_content': [noticia], 'source': [origem]})
        
        # Inicializa a lista de resultados no session_state
        st.session_state.results = []
        
        # Cria um placeholder para atualizar a interface com os resultados parciais
        placeholder = st.empty()
        
        futures = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=18) as executor:
            # Submete uma tarefa para cada combinação de artigo, modelo e sinal
            for index, row in articles.iterrows():
                for model in models:
                    for credibility_signal in dict_credibility_signals.keys():
                        future = executor.submit(
                            process_credibility_signal,
                            index, row, model, credibility_signal,
                            dict_credibility_signals, temperature=0.1, delay=1
                        )
                        # Registra o callback para adicionar o resultado à lista
                        future.add_done_callback(add_result_callback)
                        futures.append(future)
            
            # Enquanto nem todas as tarefas estiverem concluídas, atualiza o placeholder
            while not all(f.done() for f in futures):
                # Exibe os resultados parciais
                placeholder.dataframe(pd.DataFrame(st.session_state.results))
            
            # Atualiza a última vez após a conclusão de todas as tarefas
            placeholder.dataframe(pd.DataFrame(st.session_state.results))
        
        st.success("Análise concluída!")