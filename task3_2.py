

#     2. Create a simple Recurrent Neural Network (RNN) for sequence prediction (e.g., a sine wave or character prediction).


import numpy as np
# import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# Generate a sine wave dataset
time = np.linspace(0, 10, 500)
amplitude = np.sin(time)

# Create sequences for training
sequence_length = 50
sequences = []
targets = []
for i in range(len(amplitude) - sequence_length):
    sequences.append(amplitude[i:i + sequence_length])
    targets.append(amplitude[i + sequence_length])

sequences = np.array(sequences)
targets = np.array(targets)

# Reshape data for RNN
sequences = sequences.reshape(sequences.shape[0], sequences.shape[1], 1)

# Build the RNN model
model = keras.Sequential([
    keras.layers.SimpleRNN(units=50, activation='relu', input_shape=(sequence_length, 1)),
    keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(sequences, targets, epochs=50, batch_size=32)


# Make predictions
predictions = model.predict(sequences)


# Plot results
plt.plot(time[sequence_length:], amplitude[sequence_length:], label='Actual')
plt.plot(time[sequence_length:], predictions, label='Predicted')
plt.legend()
plt.show()












