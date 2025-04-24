import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r"C:\Users\mehta\OneDrive\Desktop\12302869 PY\Global_Cybersecurity_Threats_2015-2024.csv"
df = pd.read_csv(file_path)

# Inspect the data
print(df.head())
print(df.info())

# Set Seaborn theme
sns.set(style="whitegrid")

# Top 10 countries by total financial loss
top_countries = df.groupby("Country")["Financial Loss (in Million $)"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette="Reds_r", hue=None, legend=False)
plt.title("Top 10 Countries by Total Financial Loss (in Million $)")
plt.xlabel("Total Financial Loss (Million $)")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

# Number of incidents per year
attacks_per_year = df["Year"].value_counts().sort_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x=attacks_per_year.index, y=attacks_per_year.values, marker="o", color="blue")
plt.title("Number of Cybersecurity Incidents Over the Years")
plt.xlabel("Year")
plt.ylabel("Number of Incidents")
plt.xticks(attacks_per_year.index, rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Count of each attack type
attack_type_counts = df["Attack Type"].value_counts()

plt.figure(figsize=(12, 6))
sns.barplot(x=attack_type_counts.values, y=attack_type_counts.index, palette="coolwarm", hue=None, legend=False)
plt.title("Most Common Types of Cyberattacks (2015–2024)")
plt.xlabel("Number of Incidents")
plt.ylabel("Attack Type")
plt.tight_layout()
plt.show()

# Targeted industries count
industry_counts = df["Target Industry"].value_counts()

plt.figure(figsize=(12, 6))
sns.barplot(x=industry_counts.values, y=industry_counts.index, palette="viridis", hue=None, legend=False)
plt.title("Most Targeted Industries by Cyberattacks")
plt.xlabel("Number of Incidents")
plt.ylabel("Target Industry")
plt.tight_layout()
plt.show()

# Frequency of vulnerability types
vuln_counts = df["Security Vulnerability Type"].value_counts()

plt.figure(figsize=(12, 6))
sns.barplot(x=vuln_counts.values, y=vuln_counts.index, palette="magma", hue=None, legend=False)
plt.title("Most Common Security Vulnerabilities")
plt.xlabel("Number of Incidents")
plt.ylabel("Vulnerability Type")
plt.tight_layout()
plt.show()

# Average resolution time by attack type
avg_resolution_time = df.groupby("Attack Type")["Incident Resolution Time (in Hours)"].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x=avg_resolution_time.values, y=avg_resolution_time.index, palette="cividis", hue=None, legend=False)
plt.title("Average Incident Resolution Time by Attack Type")
plt.xlabel("Avg. Resolution Time (Hours)")
plt.ylabel("Attack Type")
plt.tight_layout()
plt.show()

# Heatmap: Correlation between numerical features
plt.figure(figsize=(10, 6))
numerical_features = df[[
    "Financial Loss (in Million $)", 
    "Number of Affected Users", 
    "Incident Resolution Time (in Hours)"
]]
corr = numerical_features.corr()

sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap Between Numerical Features")
plt.tight_layout()
plt.show()

# Box plots for numerical distributions
plt.figure(figsize=(18, 5))

# Financial Loss
plt.subplot(1, 3, 1)
sns.boxplot(y=df["Financial Loss (in Million $)"], color="skyblue")
plt.title("Box Plot - Financial Loss (in Million $)")

# Number of Affected Users
plt.subplot(1, 3, 2)
sns.boxplot(y=df["Number of Affected Users"], color="salmon")
plt.title("Box Plot - Number of Affected Users")

# Incident Resolution Time
plt.subplot(1, 3, 3)
sns.boxplot(y=df["Incident Resolution Time (in Hours)"], color="lightgreen")
plt.title("Box Plot - Incident Resolution Time (in Hours)")

plt.tight_layout()
plt.show()
# Scatter plot: Financial Loss vs. Number of Affected Users
plt.figure(figsize=(12, 6))
sns.scatterplot(
    data=df,
    x="Number of Affected Users",
    y="Financial Loss (in Million $)",
    hue="Attack Type",  # Color by Attack Type (optional)
    alpha=0.7,
    palette="Set2"
)

plt.title("Financial Loss vs. Number of Affected Users")
plt.xlabel("Number of Affected Users")
plt.ylabel("Financial Loss (in Million $)")
plt.legend(title="Attack Type", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()