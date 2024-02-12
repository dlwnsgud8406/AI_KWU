import tensorflow as tf
from tensorflow.keras import layers, models, Sequential
from tensorflow.keras.models import load_model

### load cifar 10 data
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

### Model construct(you can change the format
### But, you have to use the fixed name varaible 'model' as the CNN model.
### Implement the model based on Homework1 proposal.
model = models.Sequential([
  layers.Conv2D(64, kernel_size = (5, 5), strides = (1, 1), padding = 'same', activation = 'relu'),
  layers.MaxPooling2D(pool_size = (2, 2), strides = (2, 2), padding='same'),
  layers.Conv2D(64, kernel_size = (5, 5), strides = (1, 1), padding = 'same', activation = 'relu'),
  layers.MaxPooling2D(pool_size = (2, 2), strides = (2, 2), padding='same'),
  layers.Conv2D(64, kernel_size = (5, 5), strides = (1, 1), padding = 'same', activation = 'relu'),
  layers.Conv2D(128, kernel_size = (3, 3), strides = (1, 1), padding = 'same', activation = 'relu'),
  layers.Conv2D(128, kernel_size = (3, 3), strides = (1, 1), padding = 'same', activation = 'relu'),
  layers.Flatten(),
  layers.Dense(1024, activation='relu'),
  layers.Dropout(0.5),
  layers.Dense(10, activation='softmax')
])

model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics=['accuracy']) # adam, crossentropy

with tf.device("/device:GPU:0"): # use GPU
    model.fit(x_train, y_train, epochs=5)

### save the trained model
model.save('model1.h5')

### load the model (Make sure the model is saved correctly)
loaded_model = models.load_model('model1.h5')

### check the model structure (Make sure the model is saved correctly)
loaded_model.summary()

### evaluate the model with test set.
loaded_model.evaluate(x_test, y_test)