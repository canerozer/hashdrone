import tensorflow as tf
import numpy as np

class warehouse():
    def __init__(self, position, products):
        self.products = products
        self.position = position

class order():
    def __init__(self, position, products, n_products):
        self.position = position
        self.products = [0 for i in xrange(n_products)]
        for i in products:
            self.products[i] += 1

class drone():
    def __init__(self, position, n_products):
        self.position = position
        self.load = 0
        self.products = [0 for i in xrange(n_products)]
