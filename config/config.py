"""
Configurações do projeto de detecção de fake news
"""
import os
from pathlib import Path

# Diretórios do projeto
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RESULTS_DIR = PROJECT_ROOT / "results"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
APPS_DIR = PROJECT_ROOT / "apps"
SRC_DIR = PROJECT_ROOT / "src"

# Configurações de API
API_KEYS = {
    "openai": os.getenv("OPENAI_API_KEY"),
    "google": os.getenv("GOOGLE_API_KEY"), 
    "deepseek": os.getenv("DEEPSEEK_API_KEY"),
    "anthropic": os.getenv("ANTHROPIC_API_KEY")
}

# Modelos disponíveis
AVAILABLE_MODELS = {
    "openai": ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo"],
    "google": ["gemini-1.5-flash", "gemini-1.5-pro"],
    "deepseek": ["deepseek-chat"],
    "anthropic": ["claude-3-5-sonnet", "claude-3-haiku"]
}

# Configurações de processamento
DEFAULT_TEMPERATURE = 0.1
DEFAULT_DELAY = 0
DEFAULT_MAX_WORKERS = 5

# Sinais de credibilidade
CREDIBILITY_SIGNALS = {
    'Evidence': 'Does the article present any supporting evidence or arguments to substantiate its claims?',
    'Bias': 'Does the article exhibit any explicit biases in its content, tone, or perspective?',
    'Inference': 'Does the article make claims about correlation and causation?',
    'Explicitly Unverified Claims': 'Does the article contain claims that are explicitly unverified?',
    'Personal Perspective': 'Does the article express the author\'s opinion on the subject?',
    'Emotional Valence': 'Is the language in the article extremely negative or extremely positive instead of neutral?',
    'Polarising Language': 'Does the article make use of polarising terms or make divisions into sharply contrasting groups or sets of opinions or beliefs?',
    'Call to Action': 'Does the article contain language that can be understood as a call to action, requesting readers to follow through with a particular task or telling readers what to do?',
    'Expert Citation': 'Does the article cite one or more experts in the subject?',
    'Document Citation': 'Does the article cite one or more studies or documents?',
    'Source Credibility': 'Does the article cite sources that are generally considered credible?',
    'Incorrect Spelling': 'Does the article have significant misspellings and/or grammatical errors?',
    'Informal Tone': 'Does the article make use of all caps or consecutive exclamation or question marks?',
    'Incivility': 'Does the article make use of stereotypes and generalizations of groups of people?',
    'Impoliteness': 'Does the article contain insults, name-calling, or profanity?',
    'Sensationalism': 'Does the article make use of sensationalist claims?'
}
