#!/usr/bin/env python

import tensorflow as tf

x = [1, 2, 3, 4]
y = [2.1, 4.1, 6.1, 8.1]


W = tf.Variable(tf.random_normal([1]), dtype=tf.float32)
b = tf.Variable(tf.random_normal([1]), dtype=tf.float32)

H = W*x + b

cost = tf.reduce_mean(tf.square(H-y))
opt = tf.train.GradientDescentOptimizer(0.01)
do_train = opt.minimize(cost, name='do_train')

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2000):
    sess.run(do_train)
    if step%100 == 0:
        cost_out = sess.run(cost)
        W_out = sess.run(W)
        b_out = sess.run(b)
        print(step, "session... cost", cost_out, "W", W_out, "b", b_out)
