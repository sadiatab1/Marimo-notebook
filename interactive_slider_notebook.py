# Email: 23f3004490@ds.study.iitm.ac.in
# Interactive Data Analysis Notebook using Marimo
# ------------------------------------------------
# This notebook demonstrates variable dependencies,
# interactivity with a slider, and dynamic markdown
# for self-documentation.

import marimo
import numpy as np
import pandas as pd

app = marimo.App()

# Cell 1: Define a slider widget
# This slider controls the sample size `n` for data generation
sample_slider = app.slider(
    label="Select sample size (n)",
    min=10,
    max=500,
    step=10,
    value=100
)

# Cell 2: Generate dataset
# `n` comes from the slider → generates a dataset of `x` and `y`
@app.cell
def generate_data(sample_slider):
    n = sample_slider.value
    np.random.seed(42)
    x = np.linspace(0, 10, n)
    noise = np.random.normal(0, 1, n)
    y = 2 * x + 3 + noise  # Linear relation with noise
    data = pd.DataFrame({"x": x, "y": y})
    return n, data

# Cell 3: Summary statistics
# Depends on dataset generated above
@app.cell
def compute_summary(data):
    summary = data.describe().round(2)
    return summary

# Cell 4: Dynamic markdown output
# Updates whenever sample size `n` or dataset changes
@app.cell
def dynamic_output(n, summary):
    return app.markdown(f"""
    ## 📊 Data Analysis Report  
    - Current sample size: **{n}**
    - Dataset summary:  

    {summary.to_markdown()}
    """)

app.run()
