DATA_DIR = '/home/verena/data/MagnaTagATune/'
BASE_DIR = '/home/verena/data/MagnaTagATune/sampleCNN-data/'  # data dir for this model
MTT_DIR = '/home/verena/data/MagnaTagATune/mp3/'  # MTT data dir
AUDIO_DIR = '/home/verena/data/MagnaTagATune/mp3_to_npy/'
ANNOT_FILE = '/home/verena/data/MagnaTagATune/annotations_final.csv'
LIST_OF_TAGS = '/home/verena/data/MagnaTagATune/sampleCNN-data/50_tags.txt'

DEVICE_IDS=[0,1]

# audio params 
SR = 22050
NUM_SAMPLES = 59049
NUM_TAGS = 50

# train params 
BATCH_SIZE = 32
LR = 0.008
DROPOUT = 0.5
NUM_EPOCHS = 100
