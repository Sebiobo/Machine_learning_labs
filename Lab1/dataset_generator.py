
import math
import random
import csv
import matplotlib.pyplot as plt

zones = [
    {"name": "Zone 1", "mean_x": -200, "mean_y": 200, "sigma_x": 30, "sigma_y": 40},
    {"name": "Zone 2", "mean_x": 100, "mean_y": 150, "sigma_x": 40, "sigma_y": 30},
    {"name": "Zone 3", "mean_x": -100, "mean_y": -150, "sigma_x": 50, "sigma_y": 50}
]


def gaussian(x, mean, sigma):
    return math.exp(-((mean - x) ** 2) / (2 * sigma ** 2))


def generate_coordinate(mean, sigma):
    while True:
        candidate = random.uniform(-300, 300)
        probability = gaussian(candidate, mean, sigma)
        random_probability = random.random()

        if probability > random_probability:
            return candidate



def generate_point(zone):
    x = generate_coordinate(zone["mean_x"], zone["sigma_x"])
    y = generate_coordinate(zone["mean_y"], zone["sigma_y"])

    return {
        "x": x,
        "y": y,
        "zone": zone["name"],
        "type": "Normal"
    }


def generate_noise_points(zone, number_of_points=10):
    noise_points = []

    while len(noise_points) < number_of_points:
        x = random.uniform(-300, 300)
        y = random.uniform(-300, 300)

        distance = math.sqrt(
            ((x - zone["mean_x"]) / zone["sigma_x"]) ** 2
            + ((y - zone["mean_y"]) / zone["sigma_y"]) ** 2
        )

        if distance >= 4:
            noise_points.append({
                "x": x,
                "y": y,
                "zone": zone["name"],
                "type": "Noise"
            })

    return noise_points


points = []

for current_zone in zones:
    for _ in range(990):
        points.append(generate_point(current_zone))

    points.extend(generate_noise_points(current_zone, 10))

random.shuffle(points)

with open("points.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["x", "y", "zone", "type"])

    for point in points:
        writer.writerow([
            point["x"],
            point["y"],
            point["zone"],
            point["type"]
        ])


colors = {
    "Zone 1": "red",
    "Zone 2": "blue",
    "Zone 3": "green"
}

for current_zone in zones:
    zone_name = current_zone["name"]
    color = colors[zone_name]

    normal_points = [
        point for point in points
        if point["zone"] == zone_name
        and point["type"] == "Normal"
    ]

    noise_points = [
        point for point in points
        if point["zone"] == zone_name
        and point["type"] == "Noise"
    ]

    plt.scatter(
        [point["x"] for point in normal_points],
        [point["y"] for point in normal_points],
        s=10,
        color=color,
        label=zone_name
    )

    plt.scatter(
        [point["x"] for point in noise_points],
        [point["y"] for point in noise_points],
        s=10,
        color=color,
        label=f"{zone_name} Noise"
    )

plt.xlabel("X coordinate")
plt.ylabel("Y coordinate")
plt.title("Training Dataset - 3000 Points")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.show()

print("Dataset generation completed!")
print("Total number of points:", len(points))
print("Normal points:", sum(1 for p in points if p["type"] == "Normal"))
print("Noise points:", sum(1 for p in points if p["type"] == "Noise"))
print("Dataset saved to points.csv")
