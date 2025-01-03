import aisuite as ai
import pandas as pd
#import time

def create_analysis_prompt(article):
    return {
        "role": "system",
        "content": f'''
        I want you to assist me on fact-checking news articles.
        I will provide the whole article text.
        Does this article contain misinformation or propaganda? 
        Provide a detailed explanation and classify it as either "YES" or "NO".
        Below is the article:
        "{article}"
        '''
    }

def create_label_prompt(resposta):
    return {
        "role": "system",
        "content": f'''
        I will provide you with a question and the answer to that question.
        Your job is to classify the answer into two possible categories.
        They are either "YES" or "NO".
        Q: Does this article contain misinformation or propaganda?
        A: {resposta}
        Category:
        '''
    }

def create_credibility_signal_prompt(article):
    return {"role": "system", "content":
        f'''I want you to assist me on fact checking news articles.
        I will provide the whole article text, then I will ask a
        series of questions about the content of the article.
        You may elaborate objectively on the answer.
        Below is the article we will analyse:
        "{article}" 
        '''}
        

def create_weak_label_prompt(question, resposta):
    return {"role": "system", "content":
                    f'''I will provide you with a question and the answer to that question.
        Your job is to classify the answer into three possible categories.
        You may only answer with the name of the category.
        They are "YES", "NO", and "ABSTAIN".
        Q: {question}
        A: {resposta}
        Category:'''}


def zero_prompt_run(articles : pd.DataFrame, models: list, temperature=0.1):
    client = ai.Client()
    respostas = []
    for index, row in articles.iterrows():
        print(f"Processando artigo {index + 1} de {len(articles)}...")
        article = row['article_content']
        for model in models:
            try:
                messages = [create_analysis_prompt(article)]

                response = client.chat.completions.create(
                    model=model,
                    messages=messages,
                    temperature=temperature 
                )
                resposta = response.choices[0].message.content
                if resposta.str.contains('YES') or resposta.str.contains('NO'):
                    respostas.append({
                        'modelo': model,
                        'artigo': article,
                        'resposta': resposta,
                        'label': 'YES\n' if 'YES' in resposta else 'NO\n'
                    })
                else:
                    messages = [create_label_prompt(resposta)]
                    
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


def weak_supervision_label(articles : pd.DataFrame, models: list, dict_credibility_signals: dict, temperature = 0.1):
    client = ai.Client()
    respostas = []
    for index, row in articles.iterrows():
        print(f"Processando artigo {index + 1} de {len(articles)}...")
        article = row['article_content']
        for model in models:
            try:
                for credibility_signal in dict_credibility_signals.keys():
                    messages = [create_credibility_signal_prompt(article)]
                    
                    question = dict_credibility_signals[credibility_signal].format(organization_name = row['source'])

                    messages.append(
                    {"role": "system", "content":
                    f'''{question}'''})

                    response = client.chat.completions.create(
                        model=model,
                        messages=messages,
                        temperature=temperature
                    )
                    #time.sleep(1)

                    resposta = response.choices[0].message.content
                    if resposta.str.contains('Yes') or resposta.str.contains('No'):
                        respostas.append({
                            'modelo': model,
                            'artigo': article,
                            'resposta': resposta,
                            'label': 'YES\n' if 'Yes' in resposta else 'NO\n'
                        })
                    else:
                        messages.append(create_weak_label_prompt(question, resposta))

                    #time.sleep(1)
                    
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
