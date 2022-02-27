

import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np

objects = tf.keras.datasets.mnist
(training_images,training_label),(test_images, test_labels)=objects.load_data()

for i in range(9):
  plt.subplot(330+1+i)
  plt.imshow(training_images[i])

print(training_images.shape)
print(training_images[0])

training_images = training_images / 255.0
test_images = test_images / 255.0

model = tf.keras.models.Sequential([tf.keras.layers.Flatten(input_shape=(28,28)),
                                  tf.keras.layers.Dense(128,activation='relu'),
                                  tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

model.compile(optimizer = tf.keras.optimizers.Adam(),
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_images, training_label, epochs=5)

plt.imshow(test_images[0])
