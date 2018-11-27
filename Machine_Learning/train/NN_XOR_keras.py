#!/usr/bin/env python

import tensorflow as tf
#import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D

#x = tf.placeholder(tf.float32, [None, 2])
#y = tf.placeholder(tf.float32, [None, 1])

x = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [[0],[1],[1],[0]]

model = Sequential()
model.add(Dense(10, input_dim=2, activation='sigmoid'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x, y, epochs=10)

print(model.evaluate(x, y))

