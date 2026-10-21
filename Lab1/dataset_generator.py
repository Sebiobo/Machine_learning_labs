
import math
import random
import csv
import matplotlib.pyplot as plt


zones = [
    {
        "name": "Zone 1",
        "mean_x": -200,
        "mean_y": 200,
        "sigma_x": 30,
        "sigma_y": 40
    },
    {
        "name": "Zone 2",
        "mean_x": 100,
        "mean_y": 150,
        "sigma_x": 40,
        "sigma_y": 30
    },
    {
        "name": "Zone 3",
        "mean_x": -100,
        "mean_y": -150,
        "sigma_x": 50,
        "sigma_y": 50
    }
]


def gaussian(x, mean, sigma):
    result = math.exp(
        -((mean - x) ** 2) / (2 * sigma ** 2)
    )
    return result


def generate_coordinate(mean, sigma):
    while True:
        candidate = random.uniform(-300, 300)

        probability = gaussian(candidate, mean, sigma)
        random_probability = random.random()

        if probability > random_probability:
            return candidate


def generate_point(zone):
    x = generate_coordinate(
        zone["mean_x"],
        zone["sigma_x"]
    )

    y = generate_coordinate(
        zone["mean_y"],
        zone["sigma_y"]
    )

    return x, y


points = []

for current_zone in zones:
    for _ in range(1000):
        x, y = generate_point(current_zone)

        point = {
            "x": x,
            "y": y,
            "zone": current_zone["name"]
        }

        points.append(point)


random.shuffle(points)


# 7. Save the dataset to a CSV file
with open(
    "points.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:
    writer = csv.writer(file)

    writer.writerow(["x", "y", "zone"])

    for point in points:
        writer.writerow([
            point["x"],
            point["y"],
            point["zone"]
        ])


colors = {
    "Zone 1": "red",
    "Zone 2": "blue",
    "Zone 3": "green"
}

for current_zone in zones:
    zone_name = current_zone["name"]

    x_values = [
        point["x"]
        for point in points
        if point["zone"] == zone_name
    ]

    y_values = [
        point["y"]
        for point in points
        if point["zone"] == zone_name
    ]

    plt.scatter(
        x_values,
        y_values,
        s=10,
        color=colors[zone_name],
        label=zone_name
    )


plt.xlabel("X coordinate")
plt.ylabel("Y coordinate")
plt.title("Training Dataset - 3000 Points")
plt.legend()
plt.grid(True)
plt.axis("equal")

plt.savefig("points_plot.png", dpi=150)
plt.show()


print("Dataset generation completed!")
print("Total number of points:", len(points))
print("Dataset saved to points.csv")
print("Plot saved to points_plot.png")
