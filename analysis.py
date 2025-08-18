# Employee Performance Analysis
# Email: 22f3001098@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mpld3
from io import StringIO

# ---- Inline sample dataset (replace with real data if you want) ----
csv_data = """employee_id,department,region,performance_score,years_experience,satisfaction_rating
EMP001,Operations,Asia Pacific,83.27,8,3
EMP002,Operations,North America,84.03,11,3.7
EMP003,R&D,Middle East,70.68,10,3.8
EMP004,Sales,Africa,60.87,1,4.7
EMP005,Marketing,Latin America,78.6,8,3.2
EMP006,Marketing,Asia Pacific,81.2,6,4.1
EMP007,Operations,Europe,75.5,4,3.9
EMP008,HR,North America,68.4,3,4.2
EMP009,Sales,Asia Pacific,72.0,5,3.6
EMP010,Marketing,Europe,90.1,12,4.5
"""
data = pd.read_csv(StringIO(csv_data))

# ---- Step 1: Frequency count for Marketing ----
marketing_count = (data['department'] == 'Marketing').sum()
print(f"Frequency count for Marketing department: {marketing_count}")

# ---- Step 2: Plot histogram of department distribution ----
plt.figure(figsize=(8, 6))
sns.countplot(x="department", data=data, palette="viridis")
plt.title("Employee Distribution Across Departments")
plt.xticks(rotation=30)
plt.tight_layout()

# ---- Step 3: Save interactive plot as HTML ----
html_str = mpld3.fig_to_html(plt.gcf())
with open("employee_performance.html", "w") as f:
    f.write(html_str)
