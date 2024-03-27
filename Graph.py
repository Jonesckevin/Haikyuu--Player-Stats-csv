import pandas as pd
import matplotlib.pyplot as plt

# Define the column names
school_name = "School Name"
school = "School"
year = "Year"
name = "Name"
power = "Power"
jumping = "Jumping"
stamina = "Stamina"
game_sense = "Game-sense"
technique = "Technique"
speed = "Speed"
overall = "Overall"
number = "Number"
position = "Position"

# Read the CSV file
df = pd.read_csv("Haikyuu-Player-Stats.csv")

# Create a graph for each school showing scores per player
for school, data in df.groupby(school_name):
    plt.figure(figsize=(10, 6))
    plt.plot(data[name], data[overall], marker="o", linestyle="-")
    plt.xlabel("Player Name")
    plt.ylabel("Overall")
    plt.title(f"Scores per Player - {school}")
    plt.xticks(rotation=45)
    plt.show()

# Calculate average overall score per school
average_scores = df.groupby(school_name)[overall].mean()

# Create a bar graph of average overall scores per school
plt.figure(figsize=(10, 6))
plt.bar(average_scores.index, average_scores)
plt.xlabel("School Name")
plt.ylabel("Average Overall Score")
plt.title("Average Overall Score per School")
plt.xticks(rotation=45)
plt.show()

# Calculate high and low average scores per school
high_scores = df.groupby(school_name)[overall].max()
low_scores = df.groupby(school_name)[overall].min()

# Create a line graph of high and low average scores per school
plt.figure(figsize=(10, 6))
high_scores.plot(kind="line", label="High Score")
low_scores.plot(kind="line", label="Low Score")
plt.xlabel("School Name")
plt.ylabel("Average Overall Score")
plt.title("High and Low Average Scores per School")
plt.legend()
plt.xticks(rotation=45)
plt.show()

# Read the CSV file
df = pd.read_csv("Haikyuu-Player-Stats.csv")
# Create a graph for each school showing scores per player
for school, data in df.groupby("School Name"):
    plt.figure(figsize=(10, 6))
    plt.plot(data["Player Name"], data["Overall"], marker="o", linestyle="-")
    plt.xlabel("Player Name")
    plt.ylabel("Overall")
    plt.title(f"Scores per Player - {school}")
    plt.xticks(rotation=45)
    plt.show()
# Calculate average overall score per school
average_scores = df.groupby("School Name")["Overall"].mean()

# Create a bar graph of average overall scores per school
plt.figure(figsize=(10, 6))
average_scores.plot(kind="bar")
plt.xlabel("School Name")
plt.ylabel("Average Overall Score")
plt.title("Average Overall Score per School")
plt.xticks(rotation=45)
plt.show()

# Calculate high and low average scores per school
high_scores = df.groupby("School Name")["Overall"].max()
low_scores = df.groupby("School Name")["Overall"].min()

# Create a line graph of high and low average scores per school
plt.figure(figsize=(10, 6))
high_scores.plot(kind="line", label="High Score")
low_scores.plot(kind="line", label="Low Score")
plt.xlabel("School Name")
plt.ylabel("Average Overall Score")
plt.title("High and Low Average Scores per School")
plt.legend()
plt.xticks(rotation=45)
plt.show()