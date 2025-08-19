# Email: 23f3004490@ds.study.iitm.ac.in

import marimo

app = marimo.App()

# Cell 1: Define a slider widget
# This widget controls the value of `x`, which is used downstream
slider = app.slider(label="Choose a value for x", min=0, max=100, step=1, value=50)

# Cell 2: Compute a dependent variable
# `y` depends on the slider's value `x`
@app.cell
def compute_y(slider):
    x = slider.value
    y = x ** 2
    return x, y

# Cell 3: Dynamic markdown output
# This markdown updates based on the current value of `x` and `y`
@app.cell
def dynamic_output(x, y):
    return app.markdown(f"""
    ### 📊 Slider Output Summary
    - Selected value of `x`: **{x}**
    - Computed value of `y = x²`: **{y}**
    """)

app.run()

