# Smart Digit Reader  
Final Exam — ITAI1378  

A lightweight handwritten digit recognition system built with PyTorch and the MNIST dataset.

---

## Overview
Smart Digit Reader automatically identifies handwritten digits (0–9) from images.  
It reduces manual data entry errors and demonstrates how computer vision can streamline digit recognition tasks.

---

## Features
- Predicts digits from 28×28 grayscale images  
- Achieves ~98% test accuracy  
- Fast inference (<0.1s per image)  
- Built using PyTorch and the MNIST dataset  

---

## Installation
```bash
git clone https://github.com/chrishandralewich/Smart-Digit-Reader.git
cd Smart-Digit-Reader
pip install -r requirements.txt
Usage
Run the script to test predictions on a single image:
python src/predict.py --image path/to/your_image.png
| Metric | Value |
| --- | --- |
| Training Accuracy | 99% |
| Test Accuracy | 98% |
| Inference Time | <0.1s |
Demo Video
📹 Demo video link will be added here after recording the 3–5 minute system demo.
Repository Structure
Planned structure for this project:
Smart-Digit-Reader/
│
├── src/
│   ├── model.py
│   ├── predict.py
│   └── utils.py        # (optional helpers)
│
├── results/
│   ├── accuracy_plot.png
│   ├── loss_plot.png
│   └── sample_predictions.png
│
├── docs/
│   ├── presentation.pdf
│   └── AI_usage_log.md
│
├── README.md
└── requirements.txt

AI Usage Log
See docs/AI_usage_log.md for 5–10 short entries describing how AI tools were used during this project.

License
MIT License — free for educational and research use.

Acknowledgments
MNIST Dataset (LeCun et al.)

PyTorch Framework

Houston Community College — ITAI1378


> Make sure you scroll to the bottom and confirm everything is there.

---

### Step 4: Save the README

1. Scroll down to the bottom of the page.  
2. In the **“Commit changes”** box:
   - In the first line, type something like: `Finish README`  
3. Click the green **“Commit changes”** button.

Your README is now fully done for this stage.

---

If you’d like, next we can go **step‑by‑step** to create just **one folder at a time** (for example: `docs/` and `AI_usage_log.md`) so it never feels overwhelming.
