# Detecção de fake news com LLMs utilizando sinais de credibilidade

Rafael Lima Figueiredo

Bases Utilizadas:
- FA-KES(Fake Arabic News Dataset): O FA-KES é um conjunto de dados desenvolvido para auxiliar na detecção de notícias falsas relacionadas à guerra na Síria. Este dataset contém 804 artigos de notícias, cada um rotulado como verdadeiro (1) ou falso (0). A credibilidade de cada artigo foi determinada comparando as informações extraídas por meio de crowdsourcing com dados do Centro de Documentação de Violações na Síria (VDC).
- FakeNewsNet Dataset (PolitiFact): O FakeNewsNet Dataset (PolitiFact), focado apenas na parte das notícias, é uma base de dados composta por artigos jornalísticos verificados politicamente, provenientes da plataforma PolitiFact. Ela contém uma coleção de notícias políticas rotuladas como "verdadeiras" ou "falsas", oferecendo uma visão clara da verificação de fatos no contexto político.

Modelos utilizados:
- GPT-3.5 ou GPT-4
- Gemini-1.5-flash
- Claude 3.5
- LLaMA 3.1


TODO:
- Pesquisar outras bases- OK
- Verificar quais modelos testar - Ok
- Modelo para determinar label final usando os sinais de credibilidade


DEPOIS:
- Streamlit para disponibilização do modelo
