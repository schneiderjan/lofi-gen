import pickle
import os
from pathlib import Path
import numpy as np
import tensorflow as tf


# Unpickle the corpus
with open(os.path.join(Path.cwd(), "data", "corpus", "corpus.pkl"), "rb") as file:
    corpus = pickle.load(file)

# Continue with the rest of your code
symb = sorted(list(set(corpus)))
L_corpus = len(corpus)
L_symb = len(symb)
mapping = dict((c, i) for i, c in enumerate(symb))
reverse_mapping = dict((i, c) for i, c in enumerate(symb))

print("Total number of characters:", L_corpus)
print("Number of unique characters:", L_symb)


#Splitting the Corpus in equal length of strings and output target
length = 40
features = []
targets = []
for i in range(0, L_corpus - length, 1):
    feature = corpus[i:i + length]
    target = corpus[i + length]
    features.append([mapping[j] for j in feature])
    targets.append(mapping[target])
    
    
L_datapoints = len(targets)
print("Total number of sequences in the Corpus:", L_datapoints)



# reshape X and normalize
x = (np.reshape(features, (L_datapoints, length, 1)))/ float(L_symb)
# one hot encode the output variable
y = tf.keras.utils.to_categorical(targets) 

ds = tf.data.Dataset.from_tensor_slices((x, y))

# Pickle the dataset
with open(os.path.join(Path.cwd(), "data", "corpus", "dataset.pkl"), "wb") as file:
    pickle.dump(ds, file)

