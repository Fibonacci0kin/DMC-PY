# -*- coding: utf-8 -*-

import numpy as np
from Alexnet import alexnet2
from random import shuffle
import pandas as pd

# what to start at
START_NUMBER = 60

# what to end at
hm_data = 111

# use a previous model to begin?
START_FRESH = False

WIDTH = 200
HEIGHT = 145
LR = 1e-3
EPOCHS =10
MODEL_NAME = 'model_DMC_1/py-DMC-{}-{}-{}-epochs.model'.format(LR,'alexnetv2',EPOCHS)
EXISTING_MODEL_NAME = 'model_DMC_1/py-DMC-{}-{}-{}-epochs.model'.format(LR,'alexnetv2',EPOCHS)
file_name = 'training_data_DMC_v1_0.npy'

model = alexnet2(WIDTH, HEIGHT, LR)


if not START_FRESH:
    model.load(EXISTING_MODEL_NAME)

for i in range(EPOCHS):
    
    train_data = np.load(file_name,allow_pickle=True)
    train = train_data[:-3000]
    test = train_data[-3000:]

    X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
    Y = [i[1] for i in train]

    test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
    test_y = [i[1] for i in test]

    model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}), 
        snapshot_step=2500, show_metric=True, run_id=MODEL_NAME)

    model.save(MODEL_NAME)

