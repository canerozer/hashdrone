import tensorflow as tf
import numpy as np
from dimension_reduction import autoencoder as ae
import parser

warehouse_list, order_list, drone_list = parser.parse('busy_day.in')
warehouse_data = np.vstack([np.array(w.products, dtype=np.float32) for w in warehouse_list])
order_data = np.vstack([np.array(o.products, dtype=np.float32) for o in order_list])
random_data = np.vstack([np.random.randint(0, 10, 400).astype(np.float32) for i in xrange(240)])

data = np.concatenate([warehouse_data, order_data, random_data])
mean = np.mean(data, axis=0)
std = np.std(data, axis=0)
data = (data-mean)/std
autoencoder = ae(400, 2)

sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())

autoencoder.train(sess, 1001, data, 0.001)

data = np.expand_dims(np.squeeze(warehouse_data[1]), 0)
data = (data-mean)/std
de, en = autoencoder.decode_and_encode(sess, data)
print (data*std + mean).astype(np.int32)
print (de*std + mean).astype(np.int32)
