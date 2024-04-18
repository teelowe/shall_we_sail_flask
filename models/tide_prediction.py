class TidePrediction:
    def __init__(self, data):
        self.t = data['t']
        self.v = float(data['v'])
        self.type = data['type']

class TidePredictions:
    def __init__(self, data):
        self.predictions = [TidePrediction(pred) for pred in data['predictions']]
