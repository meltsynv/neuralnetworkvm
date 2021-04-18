from NeuralNetwork import NeuralNetwork
from Matrix import Matrix

nn = NeuralNetwork(2, 2, 1)

input_data = [
    [1],
    [0]
]

output_data = [
    [1]
]

print(nn.train(input_data, output_data))
