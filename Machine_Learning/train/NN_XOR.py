#!/usr/bin/env python
import tensorflow as tf

x = tf.placeholder(tf.float32, [None, 2])
y = tf.placeholder(tf.float32, [None, 1])

W = tf.Variable(tf.random_normal([2, 10]), dtype=tf.float32)
b = tf.Variable(tf.random_normal([10]), dtype=tf.float32)
layer1 = tf.sigmoid(tf.matmul(x, W) + b)

W2 = tf.Variable(tf.random_normal([10, 1]), dtype=tf.float32)
b2 = tf.Variable(tf.random_normal([1]), dtype=tf.float32)

H = tf.sigmoid(tf.matmul(layer1, W2) + b2)

cost = -tf.reduce_mean(y*tf.log(H) + (1-y)*tf.log(1-H))

do_train = tf.train.GradientDescentOptimizer(0.1).minimize(cost)

predict = tf.cast(H > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predict,y), dtype=tf.float32))

sess = tf.Session()

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
XOR_Y = [[0],[1],[1],[0]]

sess.run(tf.global_variables_initializer())

for step in range(10001):
     sess.run(do_train, feed_dict={x:X, y: XOR_Y})  
h, p = sess.run([H, predict], feed_dict={x:X, y: XOR_Y})
print("XOR : hypothesis=", h, "predict=", p)
print("XOR Accuracy: ", sess.run(accuracy, feed_dict={x:X, y: XOR_Y}))
