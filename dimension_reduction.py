import tensorflow as tf
import numpy as np


class autoencoder():
    def __init__(self, fun_in, bottleneck):
        self.fun_in = fun_in
        self.bottleneck = bottleneck

        self.net_in = tf.placeholder(tf.float32, [None, fun_in])
        self.lr_tf = tf.placeholder(tf.float32)

        fc_init = tf.contrib.layers.xavier_initializer()
        # fc_init = tf.random_uniform_initializer(minval=-0.03, maxval=0.03, dtype=tf.float32)
        fc_1 = tf.contrib.layers.fully_connected(inputs=self.net_in, num_outputs=self.fun_in/3*2, activation_fn=tf.nn.relu, weights_initializer=fc_init)
        fc_1 = tf.contrib.layers.fully_connected(inputs=fc_1, num_outputs=self.fun_in/2, activation_fn=tf.nn.relu, weights_initializer=fc_init)
        self.fc_bottleneck = tf.contrib.layers.fully_connected(inputs=fc_1, num_outputs=bottleneck, activation_fn=tf.nn.relu, weights_initializer=fc_init)
        fc_2 = tf.contrib.layers.fully_connected(inputs=self.fc_bottleneck, num_outputs=self.fun_in/2, activation_fn=tf.nn.relu, weights_initializer=fc_init)
        fc_2 = tf.contrib.layers.fully_connected(inputs=fc_2, num_outputs=self.fun_in/3*2, activation_fn=tf.nn.relu, weights_initializer=fc_init)
        self.fc_out = tf.contrib.layers.fully_connected(inputs=fc_2, num_outputs=self.fun_in, activation_fn=lambda i: i, weights_initializer=fc_init)

        self.loss = tf.reduce_mean(tf.square(self.net_in - self.fc_out))
        #self.percentage = 100*tf.reduce_mean(tf.abs(self.net_in - fc_out)/tf.sqrt(tf.reduce_sum(tf.square(self.net_in), axis=1)))
        self.opt = tf.train.AdamOptimizer(self.lr_tf).minimize(self.loss)

    def train(self, session, iteration, data, learning_rate):
        result = 0.0
        for i in xrange(iteration):
            result += session.run([self.opt, self.loss], feed_dict={self.net_in: data, self.lr_tf: learning_rate})[1]/100.0
            if not i%100:
                print result
                result = 0.0

    def encode(self, session, data):
        return session.run(self.fc_bottleneck, feed_dict={self.net_in: data})

    def decode_and_encode(self, session, data):
        return session.run([self.fc_out, self.fc_bottleneck], feed_dict={self.net_in: data})
