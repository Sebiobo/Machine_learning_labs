import matplotlib.pyplot as plt
import random
import pandas as pd
from matplotlib.animation import FuncAnimation


k = 3


def euclidean_distance(point, centroid):
    x, y = point
    cx, cy = centroid
    return ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5


def generate_centroids(k):
    centroids = []

    for i in range(k):
        x = random.uniform(-300, 300)
        y = random.uniform(-300, 300)
        centroids.append((x, y))

    return centroids


def assign_points(data, centroids):
    clusters = [[] for _ in centroids]

    for _, row in data.iterrows():
        point = (row["x"], row["y"])
        distances = [
            euclidean_distance(point, centroid)
            for centroid in centroids
        ]
        closest_index = distances.index(min(distances))
        clusters[closest_index].append(point)
    return clusters


def update_centroids(clusters, old_centroids):
    new_centroids = []

    for i, cluster in enumerate(clusters):
        if len(cluster) == 0:
            new_centroids.append(old_centroids[i])
        else:
            mean_x = sum(point[0] for point in cluster) / len(cluster)
            mean_y = sum(point[1] for point in cluster) / len(cluster)
            new_centroids.append((mean_x, mean_y))

    return new_centroids


def kmeans_animation_data(data, initial_centroids, max_epochs=100, tol=0.001):
    centroids = list(initial_centroids)
    history = [(centroids.copy(), assign_points(data, centroids))]

    for epoch in range(1, max_epochs + 1):
        clusters = assign_points(data, centroids)
        new_centroids = update_centroids(clusters, centroids)

        movements = [
            euclidean_distance(old, new)
            for old, new in zip(centroids, new_centroids)
        ]

        centroids = new_centroids
        clusters = assign_points(data, centroids)
        history.append((centroids.copy(), clusters))

        if max(movements) <= tol:
            break

    return centroids, clusters, epoch, history


data = pd.read_csv("../Lab1/points.csv")

initial_centroids = generate_centroids(k)
initial_xs = [centroid[0] for centroid in initial_centroids]
initial_ys = [centroid[1] for centroid in initial_centroids]

centroid_colors = ["red", "blue", "green"]


plt.figure(1)
for i, centroid in enumerate(initial_centroids):
    plt.scatter(
        centroid[0],
        centroid[1],
        color=centroid_colors[i],
        marker="X",
        s=120,
        label=f"Centroid {i + 1}"
    )
plt.xlim(-300, 300)
plt.ylim(-300, 300)
plt.title("Initial centroids")
plt.legend()


plt.figure(2)
plt.scatter(data["x"], data["y"], color="gray", label="Points")
for i, centroid in enumerate(initial_centroids):
    plt.scatter(
        centroid[0],
        centroid[1],
        color=centroid_colors[i],
        marker="X",
        s=120,
        label=f"Centroid {i + 1}"
    )
plt.xlim(-300, 300)
plt.ylim(-300, 300)
plt.title("Points and initial centroids")
plt.legend()


final_centroids, final_clusters, epochs, history = kmeans_animation_data(
    data,
    initial_centroids
)

print("Number of epochs:", epochs)
print("Final centroids:", final_centroids)


fig, ax = plt.subplots(num=3)
point_artists = []

centroid_artists = []
for i in range(k):
    artist = ax.scatter(
        [],
        [],
        color=centroid_colors[i],
        marker="X",
        s=180,
        edgecolors="black",
        linewidths=1.5,
        label=f"Centroid {i + 1}",
        zorder=3
    )
    centroid_artists.append(artist)

ax.set_xlim(-300, 300)
ax.set_ylim(-300, 300)
ax.set_title("Centroid movement")
ax.legend()


def update(frame):
    centroids, clusters = history[frame]

    for artist in point_artists:
        artist.remove()
    point_artists.clear()

    for i, cluster in enumerate(clusters):
        if cluster:
            cluster_xs = [point[0] for point in cluster]
            cluster_ys = [point[1] for point in cluster]
            artist = ax.scatter(
                cluster_xs,
                cluster_ys,
                color=centroid_colors[i],
                alpha=0.45,
                s=25,
                zorder=1
            )
            point_artists.append(artist)

    for i, centroid in enumerate(centroids):
        centroid_artists[i].set_offsets([[centroid[0], centroid[1]]])

    ax.set_title(f"Centroid movement — epoch {frame}")

    return centroid_artists + point_artists


animation = FuncAnimation(
    fig,
    update,
    frames=len(history),
    interval=800,
    repeat=False,
    blit=False
)

plt.show()