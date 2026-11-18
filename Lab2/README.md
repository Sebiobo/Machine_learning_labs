# K-means Clustering

A simple Python implementation of the K-means clustering algorithm for two-dimensional points. It reads points from a CSV file, groups them into `k` clusters, and animates how the centroids move during training.

## Requirements

- Python 3
- `pandas`
- `matplotlib`

Install the required libraries with:

```bash
pip install pandas matplotlib
```

## Input data

The CSV file should contain `x` and `y` columns. Additional columns are allowed but are not used by the algorithm.

Example:

```csv
x,y,zone,type
-108.79,-154.38,Zone 3,Normal
-250.01,157.66,Zone 1,Normal
```

The script reads the file using:

```python
data = pd.read_csv("../Lab1/points.csv")
```

Adjust this path if your folder structure is different.

## How it works

1. The algorithm randomly generates `k` initial centroids.
2. Each point is assigned to its nearest centroid using Euclidean distance.
3. Each centroid is moved to the mean position of the points assigned to it.
4. The assignment and update steps repeat until centroid movement is within the tolerance or the maximum number of epochs is reached.
5. The animation displays the clusters and centroid movement.

An epoch is one full assignment and centroid update. The script prints the number of epochs and the final centroid coordinates.

## Configuration

Set the number of clusters with:

```python
k = 3
```

The algorithm uses a maximum of 100 epochs and a movement tolerance of `0.001` by default. An empty cluster keeps its previous centroid.

## Run

Run the Python script from the `Lab2` folder so that the relative CSV path resolves correctly:

```bash
python k-Means.py
```

The script opens plots for the initial centroids, the points with the initial centroids, and the animated clustering result.