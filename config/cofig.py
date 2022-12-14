TARGET_SR = 8_000
SEGMENT_DURATION = 5 # seconds
CLASSES = ["lofi", "remix"]
TRAIN_SIZE = 0.8

ROOT_DIR = "./"
DATA_DIR = f"{ROOT_DIR}data/" 
SEGMENT_DIR = f"{DATA_DIR}segments/"
RAW_CLIP_PATH = f"{DATA_DIR}raw/"

DEVICE = "cuda"