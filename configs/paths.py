from pathlib import Path

# Diretorio raiz
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Diretorios de dados
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "_01_raw"
INTERIM_DATA_DIR = DATA_DIR / "_02_interim"
PROCESSED_DATA_DIR = DATA_DIR / "_03_processed"

# Arquivos específicos
APPLICATION_TRAIN = RAW_DATA_DIR / "application_train.csv"
APPLICATION_TEST = RAW_DATA_DIR / "application_test.csv"