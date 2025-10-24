"""
Arquivo principal para executar a aplicação Streamlit
"""
import sys
from pathlib import Path

# Adiciona o diretório raiz ao path
PROJECT_ROOT = Path(__file__).parent
sys.path.append(str(PROJECT_ROOT))

if __name__ == "__main__":
    import subprocess
    import os
    
    # Muda para o diretório apps
    os.chdir(PROJECT_ROOT / "apps")
    
    # Executa o Streamlit
    subprocess.run(["streamlit", "run", "app_streamlit.py"])
