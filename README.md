# Interactive Slider Notebook (Marimo)

This notebook demonstrates a minimal, rubric-compliant Marimo app with:

- ✅ Email comment for rubric validation
- 📦 Variable dependencies across cells
- 🎛️ Interactive slider widget
- 🧠 Dynamic markdown output based on widget state
- 💬 Inline comments documenting data flow

---

## 📂 File

- `interactive_slider_notebook.py`: Main Marimo notebook

---

## 🚀 Features

| Feature                     | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| Email Comment              | `# Email: 23f3004490@ds.study.iitm.ac.in` for rubric compliance             |
| Slider Widget              | `slider` widget controls value of `x`                                       |
| Variable Dependency        | `y = x²` computed from slider value                                         |
| Dynamic Markdown           | Markdown cell updates based on `x` and `y`                                  |
| Data Flow Documentation    | Inline comments explain how data flows between cells                        |

---

## 🛠️ Usage

To run the notebook:

```bash
marimo run interactive_slider_notebook.py
