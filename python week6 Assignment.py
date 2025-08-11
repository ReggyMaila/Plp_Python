

# -----------------------------------
# Assignment: Data Analysis & Visualization
# -----------------------------------

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Make plots look nicer
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (8, 5)

# ------------------------------
# Task 1: Load and Explore the Dataset
# ------------------------------

try:
    # Load the Iris dataset from sklearn
    iris_data = load_iris(as_frame=True)
    df = iris_data.frame  # Converts to Pandas DataFrame
    
    # Display first few rows
    print("First 5 rows of the dataset:")
    display(df.head())

    # Check data types and missing values
    print("\nData Info:")
    print(df.info())

    print("\nMissing Values:")
    print(df.isnull().sum())

    # No missing values here, but if there were:
    # df.fillna(df.mean(), inplace=True)  # Example: fill missing numerical values

except FileNotFoundError:
    print("Error: Dataset file not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred while loading the dataset: {e}")

# ------------------------------
# Task 2: Basic Data Analysis
# ------------------------------

# Basic statistics
print("\nBasic Statistics:")
display(df.describe())

# Grouping by species and calculating the mean
grouped = df.groupby("target").mean()
print("\nMean of numerical columns per species (target):")
display(grouped)

# Identify patterns
print("\nObservations:")
print("- Iris setosa generally has smaller petal length/width compared to other species.")
print("- Iris virginica tends to have the largest petal length and width.")

# ------------------------------
# Task 3: Data Visualization
# ------------------------------

# 1. Line chart (example: trend over samples)
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.plot(df.index, df["petal length (cm)"], label="Petal Length")
plt.title("Sepal and Petal Length Trends")
plt.xlabel("Sample Index")
plt.ylabel("Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart (average petal length per species)
avg_petal_length = df.groupby("target")["petal length (cm)"].mean()
avg_petal_length.plot(kind="bar", color=["skyblue", "orange", "green"])
plt.title("Average Petal Length by Species")
plt.xlabel("Species (0=Setosa, 1=Versicolor, 2=Virginica)")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram (distribution of sepal width)
sns.histplot(df["sepal width (cm)"], kde=True, color="purple")
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot (relationship between sepal length and petal length)
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="target", data=df, palette="Set1")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

