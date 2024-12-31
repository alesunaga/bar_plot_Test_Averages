# Import libraries
import codecademylib  # This might be specific to Codecademy's environment
from matplotlib import pyplot as plt

# Data for plotting
unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

def create_x(t, w, n, d):
    """Generates x-axis coordinates for bars in a grouped bar chart.

    Args:
      t:  Distance between the centers of each group of bars.
      w:  Width of each individual bar.
      n:  Number of the bar within its group (starting from 1).
      d:  Total number of bars.

    Returns:
      A list of x-coordinates for the bars.
    """
    return [t*x + w*n for x in range(d)]

# Generate x-axis coordinates for each school
school_a_x = create_x(2, 0.8, 1, 5)
school_b_x = create_x(2, 0.8, 2, 5)

# Create the figure and axes
plt.figure(figsize=(10, 8))  # Set figure size
ax = plt.subplot()  # Create a single subplot

# Plot the bars
plt.bar(school_a_x, middle_school_a, label='Middle School A')
plt.bar(school_b_x, middle_school_b, label='Middle School B')

# Calculate x-coordinates for the center of each group of bars
middle_x = [(a + b) / 2.0 for a, b in zip(school_a_x, school_b_x)]

# Set x-ticks and labels
ax.set_xticks(middle_x)
ax.set_xticklabels(unit_topics)

# Add a legend
plt.legend()

# Set title and axes labels
ax.set_title('Test Averages on Different Units')
ax.set_xlabel('Unit')
ax.set_ylabel('Test Average')

# Save the plot
plt.savefig('my_side_by_side.png')

# Adjust the y-axis and add gridlines
ax.set_ylim(top=100)
ax.grid(True, axis='y', color='gray')

# Add values on top of the bars
for i, value in enumerate(middle_school_a):
    ax.text(school_a_x[i], value + 0.5, str(value), ha='center')

for i, value in enumerate(middle_school_b):
    ax.text(school_b_x[i], value + 0.5, str(value), ha='center')

# Show the plot
plt.show()
