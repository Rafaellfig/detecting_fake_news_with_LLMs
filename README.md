# Detecção de Fake News com LLMs utilizando Sinais de Credibilidade

**Autor:** Rafael Lima Figueiredo  
**Projeto:** Detecção de Fake News com LLMs utilizando Sinais de Credibilidade

## 📋 Visão Geral

Este projeto desenvolve um sistema de detecção de fake news utilizando Large Language Models (LLMs) e análise de sinais de credibilidade. O sistema combina múltiplos modelos de linguagem para extrair características de credibilidade e determinar a veracidade de notícias.

## 🎯 Objetivos

- Desenvolver um sistema robusto de detecção de fake news
- Utilizar sinais de credibilidade extraídos por LLMs
- Comparar performance de diferentes modelos de linguagem
- Implementar interface web para demonstração

## 📊 Datasets Utilizados

### FA-KES (Fake Arabic News Dataset)
- **Descrição:** Dataset desenvolvido para detecção de notícias falsas relacionadas à guerra na Síria
- **Tamanho:** 804 artigos de notícias
- **Rotulagem:** Verdadeiro (1) ou Falso (0)

### Fake.Br Corpus
- **Descrição:** Base de dados com notícias em português
- **Tamanho:** 7.200 notícias (50% verdadeiras, 50% falsas)
- **Rotulagem:** Verdadeiro (1) ou Falso (0)
- **Diversidade:** Boa cobertura de temas diversos

## 🤖 Modelos de Linguagem Utilizados

- **GPT-3.5/GPT-4** - OpenAI
- **Gemini-1.5-flash** - Google
- **DeepSeek** - DeepSeek AI

## 📁 Estrutura do Projeto

```
TCC/
├── 📊 data/                          # Datasets processados
│   ├── X_train_fakebr.csv           # Dados de treino Fake.Br
│   ├── X_test_fakebr.csv            # Dados de teste Fake.Br
│   ├── X_train_fakes.csv            # Dados de treino FA-KES
│   └── X_test_fakes.csv             # Dados de teste FA-KES
├── 📓 notebooks/                     # Jupyter notebooks
│   ├── data_exploration/            # Exploração inicial dos dados
│   │   ├── analise_inicial_bases.ipynb
│   │   └── fakebr_leitura.ipynb
│   ├── analise_resultados/          # Análise dos resultados
│   │   ├── analise_weak_supervision.ipynb
│   │   └── analise_zero_shot.ipynb
│   └── criacao_labels/              # Criação de labels
│       ├── weak_supervision_label.ipynb
│       └── zero_shot_label.ipynb
├── 💻 src/                          # Código fonte
│   ├── utils/                       # Utilitários
│   │   └── api_utils.py            # APIs de LLMs
│   ├── models/                      # Modelos ML
│   ├── data/                        # Processamento de dados
│   └── analysis/                    # Análise e métricas
├── 🎯 apps/                         # Aplicações
│   ├── app_streamlit.py             # Interface principal
│   └── teste_streamlit.py          # Interface de teste
├── ⚙️ config/                       # Configurações
│   ├── config.py                    # Configurações do projeto
│   └── lithe-window-*.json          # Chaves de API
├── 📈 results/                      # Resultados e métricas
├── 🗃️ bases_externas/              # Bases de dados externas
├── 📄 TCC_Rafael_Figueiredo_att.pdf # Documento do TCC
├── main.py                          # Execução principal
├── requirements.txt                 # Dependências
└── README.md                        # Este arquivo
```

## 🚀 Instalação e Uso

### Pré-requisitos

#### 🔧 **Sistema**
- Python 3.8+
- Git
- Jupyter Notebook

#### 🔑 **APIs e Chaves**
- **OpenAI API Key** (para GPT-3.5/GPT-4)
- **Google AI API Key** (para Gemini)
- **DeepSeek API Key** (para DeepSeek)
- **Anthropic API Key** (para Claude - opcional)

#### 📦 **Dependências Python**
- pandas, numpy, scikit-learn
- xgboost, matplotlib, seaborn
- streamlit, aisuite
- rapidfuzz, scipy
- jupyter, ipykernel

### Instalação
```bash
# Clone o repositório
git clone [URL_DO_REPOSITORIO]
cd TCC

# Instale as dependências
pip install -r requirements.txt
```

### 🔧 Configuração das APIs

1. **Configure as variáveis de ambiente:**
```bash
# OpenAI
export OPENAI_API_KEY="sua_chave_openai"

# Google AI
export GOOGLE_API_KEY="sua_chave_google"

# DeepSeek
export DEEPSEEK_API_KEY="sua_chave_deepseek"

# Anthropic (opcional)
export ANTHROPIC_API_KEY="sua_chave_anthropic"
```

2. **Ou crie um arquivo `.env` na raiz do projeto:**
```env
OPENAI_API_KEY=sua_chave_openai
GOOGLE_API_KEY=sua_chave_google
DEEPSEEK_API_KEY=sua_chave_deepseek
ANTHROPIC_API_KEY=sua_chave_anthropic
```

### Execução

#### 🚀 **Método 1: Usando o arquivo principal**
```bash
# Execute a aplicação principal
python main.py
```

#### 🎯 **Método 2: Executar diretamente**
```bash
# Execute a interface Streamlit
cd apps
streamlit run app_streamlit.py
```

#### 📓 **Método 3: Executar notebooks**
```bash
# Para análise de dados
jupyter notebook notebooks/data_exploration/

# Para análise de resultados
jupyter notebook notebooks/analise_resultados/

# Para criação de labels
jupyter notebook notebooks/criacao_labels/
```

## 🔬 Metodologia

1. **Extração de Sinais de Credibilidade:** Utilização de LLMs para extrair características de credibilidade das notícias
2. **Weak Supervision:** Criação de labels utilizando múltiplos sinais de credibilidade
3. **Zero-shot Classification:** Classificação direta usando prompts estruturados
4. **Análise Comparativa:** Comparação de performance entre diferentes modelos

## 📊 Principais Resultados

### Performance dos Modelos - Zero Shot

#### FA-KES Dataset
- **Gemini 1.5-Flash:**
  - Accuracy: 79%
  - Precision: 79% (macro avg)
  - Recall: 78% (macro avg)
  - F1-Score: 79% (macro avg)

- **DeepSeek-V3:**
  - Accuracy: 62%
  - Precision: 76% (weighted avg)
  - Recall: 62% (weighted avg)
  - F1-Score: 59% (weighted avg)

#### Fake.Br Corpus
- **Gemini 1.5-Flash:**
  - Accuracy: 49%
  - Precision: 49% (macro avg)
  - Recall: 49% (macro avg)
  - F1-Score: 48% (macro avg)

- **DeepSeek-V3:**
  - Accuracy: 49%
  - Precision: 49% (macro avg)
  - Recall: 49% (macro avg)
  - F1-Score: 48% (macro avg)

### Sinais de Credibilidade Utilizados

O projeto utiliza **15 sinais de credibilidade** para análise de notícias:

#### 📊 **Sinais de Conteúdo**
1. **Evidence (Evidência):** Verificação de evidências e argumentos de suporte
2. **Bias (Viés):** Detecção de vieses explícitos ou implícitos
3. **Inference (Inferência):** Análise de correlações e causalidades
4. **Explicitly Unverified Claims:** Detecção de alegações explicitamente não verificadas
5. **Personal Perspective:** Identificação de opiniões pessoais do autor
6. **Expert Citation:** Verificação de citações de especialistas
7. **Document Citation:** Verificação de citações de estudos ou documentos
8. **Source Credibility:** Avaliação da credibilidade das fontes citadas

#### 🎭 **Sinais Linguísticos**
9. **Emotional Valence:** Detecção de linguagem extremamente negativa ou positiva
10. **Polarising Language:** Identificação de termos polarizadores
11. **Call to Action:** Detecção de linguagem que solicita ação do leitor
12. **Incorrect Spelling:** Identificação de erros ortográficos e gramaticais
13. **Informal Tone:** Detecção de uso de maiúsculas ou pontuação excessiva
14. **Incivility:** Identificação de estereótipos e generalizações
15. **Impoliteness:** Detecção de insultos, xingamentos ou palavrões
16. **Sensationalism:** Identificação de alegações sensacionalistas

### Principais Conclusões

- **Gemini 1.5-Flash** demonstrou melhor performance no dataset FA-KES (79% accuracy)
- **DeepSeek-V3** apresentou resultados mais equilibrados entre precision e recall
- Ambos os modelos tiveram dificuldades com o dataset Fake.Br (português)
- A abordagem de **Weak Supervision** com sinais de credibilidade mostrou-se promissora
- **XGBoost** foi utilizado como modelo final para combinar os sinais de credibilidade

## 🎯 Contribuições

- **Nova Abordagem:** Desenvolvimento de um sistema híbrido combinando LLMs com sinais de credibilidade
- **Metodologia Inovadora:** Uso de Weak Supervision para criação de labels de qualidade
- **Comparação Abrangente:** Análise detalhada de múltiplos modelos de linguagem
- **Interface Prática:** Desenvolvimento de aplicação Streamlit para demonstração

## ⚠️ Limitações

- **Performance em Português:** Dificuldades dos modelos com o dataset Fake.Br (português)
- **Dependência de APIs:** Necessidade de chaves de acesso para os modelos de linguagem
- **Custo Computacional:** Uso de APIs pagas para processamento em larga escala
- **Generalização:** Necessidade de validação com datasets externos

## 🔮 Trabalhos Futuros

- **Otimização de Prompts:** Refinamento dos prompts para melhor performance em português
- **Ensemble Methods:** Combinação de múltiplos modelos para melhor precisão
- **Transfer Learning:** Adaptação de modelos para domínios específicos
- **Interface Avançada:** Desenvolvimento de dashboard mais robusto

