import tensorflow as tf
import numpy as np
from tensorflow.keras import layers, models, Sequential
from tensorflow.keras.models import load_model

### load cifar 10 data
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0


### Model construct(you can change the format
### But, you have to use the fixed name varaible 'model' as the CNN model.
### Implement the model based on Homework1 proposal.
model = models.Sequential([
  layers.Conv2D(128, kernel_size = (3, 3), padding = 'same', activation = 'relu'),
  layers.BatchNormalization(), # batch normalization
  layers.Conv2D(256, kernel_size = (3, 3),  padding = 'same', activation = 'relu'),
  layers.BatchNormalization(),# batch normalization
  layers.MaxPooling2D(pool_size = (3, 3), padding = 'same'),
  layers.BatchNormalization(),# batch normalization

  layers.Conv2D(512, kernel_size = (4, 4), padding = 'same', activation = 'relu'),
  layers.BatchNormalization(),# batch normalization
  layers.Conv2D(1024, kernel_size = (5, 5), padding = 'valid', activation = 'relu'), # padding valid
  layers.BatchNormalization(),# batch normalization
  layers.MaxPooling2D(pool_size = (7, 7), padding = 'valid'), # padding valid
  layers.BatchNormalization(),# batch normalization

  layers.Flatten(),

  layers.Dense(60, activation='sigmoid'), # sigmoid
  layers.Dropout(0.001),
  
  layers.Dense(10, activation='softmax'),

])

model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics=['accuracy'])

with tf.device("/device:GPU:0"):
    print("it it gpu")
    model.fit(x_train, y_train, epochs=5)

### save the trained model
model.save('model2.h5')

### load the model (Make sure the model is saved correctly)
loaded_model = models.load_model('model2.h5')

### check the model structure (Make sure the model is saved correctly)
loaded_model.summary()

### evaluate the model with test set.
loaded_model.evaluate(x_test, y_test)