# Email: 23f3004490@ds.study.iitm.ac.in
# Marimo Interactive Notebook Demo
# This notebook shows how variable dependencies, widgets, and dynamic markdown work.

import marimo as mo

# --------------------------
# Cell 1: Import and slider
# --------------------------
# This slider represents "sample size" for a dataset.
sample_size = mo.ui.slider(10, 500, value=100, label="Select Sample Size")
sample_size

# --------------------------
# Cell 2: Generate data based on slider
# --------------------------
# Data depends on sample_size value chosen in Cell 1.
import numpy as np
import pandas as pd

# Create synthetic dataset
x = np.linspace(0, 10, sample_size.value)
y = 2 * x + np.random.normal(0, 2, size=sample_size.value)

data = pd.DataFrame({"X": x, "Y": y})
data.head()

# --------------------------
# Cell 3: Summary statistics
# --------------------------
# This depends on Cell 2 (data).
summary = data.describe()
summary

# --------------------------
# Cell 4: Dynamic Markdown
# --------------------------
# This Markdown depends on the slider value.
mo.md(f"""
### 📊 Interactive Data Analysis

You selected **{sample_size.value}** samples.  
More samples generally make the data smoother.  

🟢 "Green dots" represent the number of samples:  
{"🟢" * (sample_size.value // 20)}
""")
