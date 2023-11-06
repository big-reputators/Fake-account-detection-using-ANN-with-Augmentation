
from import_libs import *
import netron



from dataset_load import instagram_df_train,instagram_df_test

from data_preprocess_model import X_train,y_train,X_test,y_test

# Building and Training Deep Training Model
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(11, input_dim=11, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(50, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(25, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(2,activation='softmax'))

model.summary()
optimizer=Adam(learning_rate=0.001)
model.compile(loss = 'categorical_crossentropy', metrics = ['accuracy'])

epochs_hist = model.fit(X_train, y_train, epochs = 60,  verbose = 1, validation_split = 0.1)
model.save('my_model')
keras_model = keras.models.load_model('my_model')

# Save the Keras model to a file
keras.models.save_model(keras_model, 'my_model.h5')

# Visualize the model using Netron
netron.start('my_model.h5')
