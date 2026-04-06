# Grade 7/8 Math + Python: Introduction to Applied AI

Hands-on Jupyter notebooks and data for a short classroom unit that connects **school math** (starting with the equation of a line), **Python programming**, and **machine learning / AI**. The materials were used for a week-long “Introduction to AI” in a grade 7/8 math class, with live coding and room for stronger students to extend the examples with their own functions.

You are welcome to reuse this content to help students see why math matters for technology, how coding turns math into working models, and how today’s ML and AI systems build on those ideas.

## Who this is for

- **Teachers and parents** running a multi-day intro (roughly four sessions) with laptops or lab time.
- **Students** from late elementary through high school; difficulty can be adjusted by how fast you move and how much you lean on exercises vs. demos.

## Before day 1 (recommended prerequisite)

Ask the classroom teacher to review the **equation of a line**, **y = mx + b**, shortly before you start. Class 1 ties Python and plotting to that form, and later lessons connect **slopes and intercepts** to how many ML models learn from data. That bridge from “math class last week” to “this is what computers do in AI” lands especially well when the line work is fresh.

## Four-day arc (how the notebooks map)

| Day | Focus | Main notebook(s) |
|-----|--------|------------------|
| **1** | Intro to **math programming** in Python: notebooks, variables, calculations, and connecting ideas to **y = mx + b** | `Class 1.ipynb` · optional stretch: `Class 1 Bonus Content.ipynb` |
| **2** | **Simple models**: averages, then **linear models** with real-looking examples | `Class 2.ipynb` |
| **3** | **Intro to machine learning**: multivariable **linear regression**, **decision trees**, **random forests**, comparing predictions and error | `Class 3.ipynb` |
| **4** | **Neural networks (AI)**: from digits to richer image tasks; pairs well with a **vibe-coding** or “build something together” demo (e.g. a simple game) using your slide deck and prompts | `Class 4 Neural Networks.ipynb` |

### A Note on Google Colab

- I taught this week of classes twice. One of the times, Google Colab was unavailable for the students. Classes 1-3 work just fine in Jupyter Lite (https://jupyter.org/try-jupyter/lab/). However, class 4 runs larger models and wasn't accessible in Jupyter Lite (which runs in browser) so I made an alternative class 4 notebook in that scenario. Thankfully we had IT unlock Google Colab so we could use the original, which allows the students to run CNN architecture (not possible in Jupyter Lite) but the Jupyter Lite version is there now in case others experience permissions issues too. 

## Data in this repository

- **`Data/kids anonymous data.csv`** — Anonymized classroom-style measurements (e.g. age-related fields, foot length, finger length) used in **Class 3** to predict **height** with several model types. The notebook can load this file from the web when the dataset is hosted on GitHub, or you can point students at a **local copy** in `Data/` after cloning or downloading the repo.

Treat any similar dataset you collect in your own classroom with appropriate **privacy and consent** norms; this file is intended as a teaching example.

## How to run the notebooks

1. **Google Colab** — Upload or open the `.ipynb` from GitHub; good for Class 1–3 and the TensorFlow Class 4 notebook (GPU strongly recommended).
2. **JupyterLite** — Use the Class 2–3 cells that install **`pyodide-http`** via `micropip` and the JupyterLite-oriented Class 4 / CIFAR-10 notebooks when you need **no server-side ML stack**.
3. **Jupyter Notebook / JupyterLab (local)** — A more advanced class, such as high school computer science students, would benefit from running the code on their own computers. Install Python & IDE, then packages as needed (`numpy`, `pandas`, `matplotlib`, `scikit-learn`). However, for class 4, I still recommend using Google Colab because of the ability to use Google's free GPUs & the complexity involved in setting up tensorflow locally for GPU (running the CIFAR-10 models without GPU takes prohibitively long). 

If a notebook references a **raw GitHub URL** for the CSV, either keep that URL pointed at a public copy of this repo or change the path to your local `Data/kids anonymous data.csv`.

## Optional: `Other Groundwork/`

The **`Other Groundwork/`** folder holds **advanced or preparatory** material (for example, text-processing and **nanoGPT**-style scripts and configs). It is **not** required for the four-day school sequence; it is there if you want to explore language-model-style projects on your own time.

## Related teaching materials (outside this repo)

A full classroom run can also include:

- Slide decks (**PowerPoint** or similar) for the big ideas.
- A **vibe-coding** session: one-shot or iterative prompting to build a small **game** from students’ ideas, with the generated code living in a **separate repository** for the playable build. You can give this prompt to an AI coding agent (e.g., Claude Code, Cursor) with any custom suggestions the class wants to use to make the game feel like theirs and the AI will create the game from scratch. 

## Pedagogical goal (in one paragraph)

Students should leave with an intuitive picture of **using data to make predictions**, seeing that **linear structure** (like **y = mx + b**) shows up inside many models, that **code** is how we try ideas quickly, and that **neural networks** are the next step up in complexity—not magic, but layered mathematics and computation. Stronger students get enough scaffolding to **modify and extend** the notebooks; everyone gets a honest, age-appropriate first pass at **applied AI**.

---

*If this helps your class or your kids, feel free to share the repository with other educators or families who care about applied math, coding, and AI.*
