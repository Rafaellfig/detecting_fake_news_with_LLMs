import aisuite as ai
import pandas as pd
import re
import time

def create_analysis_prompt(article):
    return [
    {
        "role": "system",
        "content": "You are an expert assistant specialized in fact-checking news articles. Your goal is to identify whether an article contains misinformation or propaganda, providing a detailed explanation and classifying the response as either 'YES' or 'NO'."
    },
    {
        "role": "user",
        "content": f"Below is the article for analysis:\n\"{article}\"\nDoes this article contain misinformation or propaganda? Provide a detailed explanation for your conclusion and classify it as either 'YES' or 'NO'."
    }
]

def create_label_prompt(resposta):
    return [{
        "role": "system",
        "content": "You are an assistant specialized in classifying answers into two possible categories: 'YES' or 'NO'. Your job is to analyze the answer provided to a specific question and determine the correct category based on the context."
    },
    {
        "role": "user",
        "content": f"Question: Does this article contain misinformation or propaganda?\nAnswer: {resposta}\n\nClassify the answer into either 'YES' or 'NO'."
    }]
    
def create_credibility_signal_prompt(article):
    return [
        {
        "role": "system",
        "content": "You are an assistant specialized in fact-checking news articles. Your job is to critically analyze news texts and answer specific questions based on verifiable evidence."
    },
    {
        "role": "user",
        "content": f"I will provide the full text of a news article, followed by a series of questions about its content. Please analyze it objectively and provide evidence-based answers. Here is the article: '{article}'"
    }]
    
def create_weak_label_prompt(question, resposta):
    return {
    "role": "system",
    "content": f'''Your task is to classify answers into three possible categories based on the question and its answer. You may only respond with the name of the category. The categories are: 'YES', 'NO', and 'ABSTAIN'.
    I will provide you with a question and its corresponding answer. Classify the answer according to the categories defined. Here is the input:\nQ: {question}\nA: {resposta}\nCategory:'''
    }


def zero_prompt_run(articles : pd.DataFrame, models: list, temperature=0.1):
    client = ai.Client()
    respostas = []
    for index, row in articles.iterrows():
        print(f"Processando artigo {index + 1} de {len(articles)}...")
        article = row['article_content']
        for model in models:
            try:
                messages = create_analysis_prompt(article)

                response = client.chat.completions.create(
                    model=model,
                    messages=messages,
                    temperature=temperature 
                )
                resposta = response.choices[0].message.content
                if isinstance(resposta, str) and re.search(r'^(YES|NO)\b', resposta, re.IGNORECASE):
                    respostas.append({
                        'modelo': model,
                        'artigo': article,
                        'resposta': resposta,
                        'label': 'YES\n' if 'YES' in resposta else 'NO\n'
                    })
                else:
                    messages = create_label_prompt(resposta)
                    
                    label = client.chat.completions.create(
                        model=model,
                        messages=messages,
                        temperature=temperature
                    )

                    label = label.choices[0].message.content
                    respostas.append({
                        'modelo': model,
                        'artigo': article,
                        'resposta': resposta,
                        'label': label
                    })
            except Exception as e:
                print(f"Error processing article {index}, with model {model}: {e}")
                continue
    df_respostas = pd.DataFrame(respostas)
    return df_respostas


def weak_supervision_label(articles : pd.DataFrame, models: list, dict_credibility_signals: dict, temperature = 0.1, delay = 0):
    client = ai.Client()
    respostas = []
    for index, row in articles.iterrows():
        print(f"Processando artigo {index + 1} de {len(articles)}...")
        article = row['article_content']
        for model in models:
            try:
                for credibility_signal in dict_credibility_signals.keys():
                    messages = create_credibility_signal_prompt(article)
                    
                    question = dict_credibility_signals[credibility_signal].format(organization_name = row['source'])

                    messages.append(
                    {"role": "user", "content":
                    f'''{question}'''})

                    response = client.chat.completions.create(
                        model=model,
                        messages=messages,
                        temperature=temperature
                    )
                    time.sleep(delay)

                    resposta = response.choices[0].message.content
                    if isinstance(resposta, str) and re.search(r'\b(YES|NO)\b', resposta.upper()):
                        resposta_final = 'YES\n' if 'YES' in resposta.upper() else 'NO\n'
                        
                    else:
                        messages.append(create_weak_label_prompt(question, resposta))

                        time.sleep(delay)
                    
                        response = client.chat.completions.create(
                            model=model,
                            messages=messages,
                            temperature=temperature
                        )

                        resposta_final = response.choices[0].message.content
                    
                    respostas.append({
                    'modelo': model,
                    'artigo': article,
                    'sinal_credibilidade': credibility_signal,
                    'pergunta': question,
                    'resposta': resposta,
                    'label': resposta_final
                })
            except Exception as e:
                print(f"Erro ao processar o artigo {index}, no modelo {model}: {e}")
                continue
        
    df_respostas = pd.DataFrame(respostas)
    return df_respostas
