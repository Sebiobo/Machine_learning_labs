# Gaussian Dataset Generator

## Overview

A Python project that generates a two-dimensional training dataset using a Gaussian function and the rejection sampling method.

The dataset contains 3,000 points distributed around three user-defined zones, with approximately 1,000 points generated for each zone.

## Features

- Define multiple zones using their centers and standard deviations.
- Generate X and Y coordinates independently using a Gaussian function.
- Use rejection sampling to accept or reject candidate coordinates.
- Generate 3,000 points across three zones.
- Shuffle the generated points to avoid grouping them by zone.
- Export the dataset to a CSV file.
- Visualize the points in a two-dimensional scatter plot.
- Save the visualization as a PNG image.

## Technologies

- **Python 3.12**
- **Matplotlib** — for data visualization.
- **CSV** — for exporting the generated dataset.
- **Math and Random** — Python standard library modules.

## Requirements

Python 3.12 or a compatible version and Matplotlib are required.

Install Matplotlib using pip:

```bash
python -m pip install matplotlib
```

## Usage

Run the generator:

```bash
python dataset_generator.py
```

The program generates the following files:

- `points.csv` — contains the generated coordinates and zone labels.
- `points_plot.png` — contains the scatter plot visualization.

## Gaussian Function

The program uses the following Gaussian function:

\[
G(x)=e^{-\frac{(m-x)^2}{2\sigma^2}}
\]

Where:

- \(x\) is the candidate coordinate.
- \(m\) is the center coordinate.
- \(\sigma\) is the standard deviation.

Candidates are generated randomly within the interval \([-300,300]\). Each candidate is accepted when its Gaussian value is greater than a random value between 0 and 1. Otherwise, another candidate is generated.

The process is applied independently to the X and Y coordinates.

## Zone Configuration

Each zone is defined by the following parameters:

| Parameter | Description |
|---|---|
| `name` | Zone identifier |
| `mean_x` | Center coordinate along the X axis |
| `mean_y` | Center coordinate along the Y axis |
| `sigma_x` | Standard deviation along the X axis |
| `sigma_y` | Standard deviation along the Y axis |

The centers and standard deviations can be modified in the `zones` list in `dataset_generator.py`.

## Output Files

### `points.csv`

Contains the generated dataset with three columns:

| Column | Description |
|---|---|
| `x` | X coordinate of the point |
| `y` | Y coordinate of the point |
| `zone` | Zone associated with the point |

The file contains 3,000 data rows and one header row.

### `points_plot.png`

Contains a scatter plot of the generated points. Each zone is displayed in a different color:

- **Zone 1:** Red
- **Zone 2:** Blue
- **Zone 3:** Green

## Educational Purpose

This project demonstrates Gaussian-based point generation, rejection sampling, basic file handling, and data visualization in Python. It was developed as an educational exercise for generating a training dataset.
