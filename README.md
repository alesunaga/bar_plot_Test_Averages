# bar_plot_Test_Averages
# Visualizing Test Averages for Two Middle Schools

This repository contains Python code that generates a grouped bar chart to visualize and compare the test averages of two middle schools (School A and School B) across different units of a subject (Limits, Derivatives, Integrals, Diff Eq, Applications).

## Data

The code uses the following lists as data:

* **`unit_topics`:** A list of unit names.
* **`middle_school_a`:** A list of test averages for each unit in School A.
* **`middle_school_b`:** A list of test averages for each unit in School B.

## Visualization

The code generates a grouped bar chart with the following features:

* **Grouped Bars:** Each unit has two bars, one for School A and one for School B, allowing for easy comparison.
* **X-axis Labels:** The x-axis is labeled with the unit names.
* **Y-axis Label:** The y-axis represents the test average.
* **Legend:** A legend indicates which bars correspond to each school.
* **Title:** The chart has a title "Test Averages on Different Units".
* **Gridlines:** Horizontal gridlines are added for better readability.
* **Value Labels:** The test average values are displayed on top of each bar.

The plot is saved as a PNG file (`my_side_by_side.png`).

## Usage

1. Make sure you have the `matplotlib` library installed. You can install it using `pip install matplotlib`.
2. Run the Python script.

## Output

The code will produce a grouped bar chart named `my_side_by_side.png` that visualizes the test averages of the two middle schools.

## Contributing

Feel free to fork this repository and contribute your own improvements or modifications.

## License

This code is released under the MIT License.
