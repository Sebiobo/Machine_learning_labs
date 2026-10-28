## Dataset Generation

The project generates a 2D training dataset containing **3,000 points** distributed across three zones using a Gaussian-based coordinate generation algorithm.

### Dataset Composition

- **2,970 normal points** generated using a Gaussian-based method.
- **30 noise points**, with 10 noise points assigned to each zone.
- **3 zones**, each represented by a different color:
  - Zone 1: Red
  - Zone 2: Blue
  - Zone 3: Green

### Noise Point Generation

Noise points are generated randomly within the coordinate range `[-300, 300]` for both X and Y. Their normalized distance from the center of their assigned zone must be at least 4, ensuring that they are located far from that zone's main cluster.

Each point is labeled as either `Normal` or `Noise`.

### Output

The generated dataset is saved to `points.csv`, containing the following columns:

- `x`: X coordinate
- `y`: Y coordinate
- `zone`: Assigned zone
- `type`: Point classification (`Normal` or `Noise`)

The dataset is also visualized using a scatter plot, allowing normal points and noise points to be inspected.
