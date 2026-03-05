DNA Sequencer & Mutation Analysis System

A web-based DNA sequence analysis tool that detects mutations, searches patterns, and predicts mutation probability using classical algorithms and machine learning.

This project was developed as a 3rd Semester Software Engineering project to demonstrate how bioinformatics algorithms and machine learning can be combined to analyze DNA sequences.

🚀 Features
🧬 DNA Mutation Detection

Compares Reference DNA and Query DNA

Detects mutation points (base differences)

Calculates mutation percentage

🔎 Pattern Search Algorithms

The project implements two efficient string-search algorithms used in bioinformatics:

KMP (Knuth-Morris-Pratt) Algorithm

Efficient exact pattern matching in DNA sequences.

Suffix Array Search

Fast substring searching using a sorted suffix structure.

📊 Sequence Alignment

Uses Needleman-Wunsch Global Alignment

Measures similarity between DNA sequences

Produces an alignment score

🤖 Mutation Probability Prediction

Uses Logistic Regression (Machine Learning)

Predicts probability of mutation intensity based on mutation density.

📈 Mutation Visualization

Graphically displays mutation positions in the DNA sequence.

📂 FASTA File Support

Users can upload FASTA formatted DNA files for analysis.

🧠 Algorithms Used
Algorithm	Purpose
KMP Algorithm	Efficient exact DNA pattern search
Suffix Array	Fast substring searching in long sequences
Needleman-Wunsch	Global DNA sequence alignment
Logistic Regression	Mutation probability prediction
🛠 Tech Stack
Programming

Python

Backend

Flask

Machine Learning

Scikit-learn

NumPy

Visualization

Matplotlib

Frontend

HTML

CSS

Bioinformatics Utilities

FASTA file reader

Mutation plot generator

📂 Project Structure
DNA-Sequencer/
│
├── app.py
│
├── algorithms/
│   ├── kmp.py
│   ├── suffix_array.py
│   ├── alignment.py
│   └── mutation.py
│
├── ml/
│   └── mutation_predictor.py
│
├── utils/
│   ├── fasta_reader.py
│   └── plotter.py
│
├── templates/
│   └── index.html
│
└── README.md
⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/yourusername/dna-sequencer.git
cd dna-sequencer
2️⃣ Install Dependencies
pip install flask numpy scikit-learn matplotlib
3️⃣ Run the Application
python app.py
4️⃣ Open in Browser
http://127.0.0.1:5000
🧪 Example Workflow

1️⃣ Enter Reference DNA sequence

Example:

ATGCGTACGTTAGCTAGCTAGGCTAGCTAG

2️⃣ Enter Query DNA sequence

Example:

ATGCGTACGTTAGCTAGCTAGGCTAGTTAG

3️⃣ Click Analyze

The system will return:

KMP Matches

Suffix Array Matches

Alignment Score

Total Mutation Points

Mutation Probability

📊 Example Output
KMP Matches: 0
Suffix Array Matches: 0
Alignment Score: 217
Total Mutation Points: 89
Mutation Probability: 60.97%
🎓 Educational Purpose

This project is designed to help students understand:

DNA sequence comparison

Bioinformatics algorithms

Pattern matching in biological data

Machine learning applications in genomics

It serves as a mini bioinformatics analysis system built using classical algorithms and modern web technologies.

⚠️ Disclaimer

This project is intended for educational and research demonstration purposes only.

It is not designed for medical or clinical genetic analysis.

👨‍💻 Author

Ayan Ahmad
Software Engineering Student
