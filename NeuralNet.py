import random as rand
import math
import sys

#sigmoid function
def sigmoid(x):
    return 1/(1+(math.e ** (-1*x)))

#derivative of x
def sigPrime(x): 
    return (math.e ** x) / (((math.e ** x) + 1) ** 2)

class Neuron:
    def __init__(self,numPrevLayer): #parameters initialized randomly on [-1 1]
        self.bias = 0#rand.uniform(-1,1);
        self.weights = []
        for k in range(0,numPrevLayer):
            self.weights.append(1)
            #self.weights.append(rand.uniform(-1,1))

    def compute(self,prevActivs):
        self.activ = sigmoid(self.compLinearActiv(prevActivs))
        return self.activ

    def compLinearActiv(self,prevActivs):
        self.linearActiv = self.bias
        for k in range(len(prevActivs)):
            self.linearActiv += self.weights[k] * prevActivs[k]
        return self.linearActiv

    def partialWeightDeriv(self,k,activK): #dalj/dwljk, activK is a(l-1)k
        return 2 * sigPrime(self.linearActiv) * self.weights[k] * (activK ** 2)

    def partialBiasDeriv(self): #dalj/dblj
        return sigPrime(self.linearActiv)

class Network:
    def __init__(self,layers):
        self.neurons = []
        for l in range(len(layers)):
            self.neurons.append([0]) #input neuron
            for j in range(1,layers[l]):
                self.neurons[l].append(Neuron(layers[l-1]))

    def compute(self,data): #data is one sample, len = num input neurons
        for l in range(len(self.neurons)):
            for j in range(len(self.neurons[l])):
                if type(self.neurons[l][j]) is float or type(self.neurons[l][j]) is int:
                    self.neurons[l][j] = sigmoid(data[j])
                else:
                    self.neurons[l][j].compute(self.neurons[l-1])

    def cost(self, data, labels): #data is all samples, labels are all labels
        self.cost = 0
        for i in range(len(data)):
            self.compute(data[i])
            for j in range(len(self.neurons[len(self.neurons)-1])):
                self.cost += (self.neurons[len(self.neurons)-1].activ - labels[i][j]) ** 2
        return self.cost

'''data file in format like:
a b c d e... (input data)
x y z...     (label)
.
.
.
'''
def loadData(fname): #read from data file to
    print("Loading data from " + fname)
    with open(fname) as f:
        data = []
        labels = []
        while True:
            line = f.readline()
            if not line:
                break
            data.append([eval(i) for i in line.split()])
            labels.append([eval(i) for i in f.readline().split()])
    return data, labels

if __name__ == "__main__": #parameters like  python Network.py dataFile layers/layerFile
    rand.seed()
    args = sys.argv
    data, labels = loadData(args[1])
    if not args[2].endswith(".txt"):
        layers = eval(args[2])

    network = Network(layers)
    network.compute(data[0])

    print("values")
    for i in network.neurons:
        for j in i:
            if type(j) is float or type(j) is int:
                print(j)
            else:
                print(j.activ)
        print("")
