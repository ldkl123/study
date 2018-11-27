#!/usr/bin/env python

import tensorflow as tf
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

x_data = mnist.train.images.reshape(-1, 28, 28, 1)
y_data = mnist.train.labels

model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3), input_shape=(28, 28, 1), activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x_data, y_data, epochs=15, batch_size=100)

print(model.evaluate(mnist.test.images.reshape(-1, 28, 28, 1), mnist.test.labels))
