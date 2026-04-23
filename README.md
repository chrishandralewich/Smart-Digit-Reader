# Smart-Digit-Reader
Final Exam ITAI1378

A lightweight handwritten digit recognition system built with PyTorch and the MNIST dataset.

Overview
Smart Digit Reader automatically identifies handwritten digits (0–9) from images.
It reduces manual data entry errors and demonstrates how computer vision can streamline digit recognition tasks.

Features
Predicts digits from 28×28 grayscale images

Achieves ~98% test accuracy

Fast inference (<0.1s per image)

Built using PyTorch and MNIST dataset
git clone https://github.com/chrishandralewich/Smart-Digit-Reader.git
cd Smart-Digit-Reader
pip install -r requirements.txt
python src/predict.py --image sample_digit.png
| Metric | Value |
| --- | --- |
| Training Accuracy | 99% |
| Test Accuracy | 98% |
| Inference Time |  |
SmartDigitReader/
│
├── notebooks/
│   └── train_model.ipynb
│
├── src/
│   ├── model.py
│   ├── predict.py
│   └── utils.py
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
See docs/AI_usage_log.md for 5–10 entries describing how AI tools assisted in development.

License
MIT License — free for educational and research use.

Acknowledgments
MNIST Dataset (LeCun et al.)

PyTorch Framework

Houston Community College — ITAI1378
