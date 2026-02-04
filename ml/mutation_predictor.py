import numpy as np
from sklearn.linear_model import LogisticRegression

# Train once (global)
X = np.array([[0.0],[0.05], [0.10], [0.20], [0.30], [0.40]])
y = np.array([0, 0, 0, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)

def predict_mutation_probability(mutation_count, dna_length):
    if dna_length == 0:
        return 0.0

    density = mutation_count / dna_length
    prob = model.predict_proba([[density]])[0][1]

    return round(prob * 100, 2)
