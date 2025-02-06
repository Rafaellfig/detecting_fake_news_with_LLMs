# Detecção de fake news com LLMs utilizando sinais de credibilidade

Rafael Lima Figueiredo

Bases Utilizadas:
- FA-KES(Fake Arabic News Dataset): O FA-KES é um conjunto de dados desenvolvido para auxiliar na detecção de notícias falsas relacionadas à guerra na Síria. Este dataset contém 804 artigos de notícias, cada um rotulado como verdadeiro (1) ou falso (0). A credibilidade de cada artigo foi determinada comparando as informações extraídas por meio de crowdsourcing com dados do Centro de Documentação de Violações na Síria (VDC).
- Fake.Br Corpus: Base de dados com 7.200 notícias em português, divididas igualmente entre verdadeiras e falsas. As notícias falsas foram coletadas de sites conhecidos por espalhar desinformação, enquanto as verdadeiras são de fontes confiáveis. Contém uma boa diversidade de temas.

Modelos utilizados:
- GPT-3.5 ou GPT-4
- Gemini-1.5-flash - Ok
- Claude 3.5
- DeepSeek
- LLaMA 3.1


TODO:
- Pesquisar outras bases- OK
- Verificar quais modelos testar - Ok
- Modelo para determinar label final usando os sinais de credibilidade
# TODO Ajustar logica user - system e ajustar prompt

DEPOIS:
- Streamlit para disponibilização do modelo
