inputs = [1, 2, 3, 2.5]

weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

ls = []
for neuron_weights, neuron_bias in zip(weights, biases):
    output = 0
    for n_input, weight in zip(inputs, neuron_weights):
        output = output + n_input * weight
    output = output + neuron_bias
    ls.append(output)
print(ls)