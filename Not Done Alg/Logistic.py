import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, metrics
from sklearn.cluster import KMeans

digits = datasets.load_digits()
_, axes = plt.subplots(nrows=1, ncols=20, figsize=(20, 6))
for ax, image, label in zip(axes, digits.images, digits.target):
    ax.set_axis_off()
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    ax.set_title("Training: %i" % label)
    

# x = digits.images.reshape(len(digits), -1)
x = digits.data[np.random.choice(digits.data.shape[0], 100)]
kmeans = KMeans(n_clusters = 9).fit(x)
pred_label = kmeans.predict(x)

for ax, image, label in zip(axes, digits.images, pred_label):
    ax.set_axis_off()
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    ax.set_title(" %i" % label)
plt.show()