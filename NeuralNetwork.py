from Matrix import Matrix
from Sigmoid import Sigmoid


class NeuralNetwork:
    input_nodes = 0
    hidden_nodes = 0
    output_nodes = 0

    weights_ih = 0
    weights_ho = 0
    bias_h = 0
    bias_o = 0

    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        # init Neural Network structure
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        # Random weights and bias initialization
        self.weights_ih = Matrix.randomize(self.hidden_nodes, self.input_nodes)
        self.weights_ho = Matrix.randomize(self.output_nodes, self.hidden_nodes)
        self.bias_h = Matrix.randomize(self.hidden_nodes, 1)
        self.bias_o = Matrix.randomize(self.output_nodes, 1)

    def feed_forward(self, values):
        # generating hidden output
        hidden = Matrix.mult(self.weights_ih, values)
        hidden = Matrix.add(hidden, self.bias_h)
        hidden = list(Sigmoid.matrix(hidden))

        # generating output nodes
        output = Matrix.mult(self.weights_ho, hidden)
        output = Matrix.add(output, self.bias_o)
        output = list(Sigmoid.matrix(output))

        return output

    def train(self, inputs, targets):
        outputs = self.feed_forward(inputs)

        # Calculate the error
        # error = targets - outputs
        output_errors = Matrix.sub(targets, outputs)

        # calculate the hidden layer errors
        weights_ho_transpose = Matrix.transpose(self.weights_ho)
        hidden_errors = Matrix.mult(weights_ho_transpose, output_errors)

        return hidden_errors
        pass

    def display_weights(self):
        print("=== Random Weights ===")
        print("Hidden Weights:", end='')
        print(* self.weights_ih)
        print("Hidden Bias:", end='')
        print(* self.bias_h)
        print("Output Weights:", end='')
        print(* self.weights_ho)
        print("Output Bias: ", end='')
        print(* self.bias_o)
