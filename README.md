# Tobii Eye Tracker: Real-Time Data Collection and Visualization Suite

This project provides a robust Python-based pipeline for capturing, processing, and visualizing gaze data from licensed Tobii hardware.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ahmet-bora-bakir/tobii-eye-tracker.git
   cd tobii-eye-tracker
2. **Create & Activate Virtual Environment (Recommended):**
   python3.10 -m venv env
# Windows:
.\env\Scripts\activate
# macOS/Linux:
source env/bin/activate
3. **Install required libraries:**
   pip install -r requirements.txt
## Tech Stack & Libraries
This project is built with the following core libraries:

* **tobii-research:** The official SDK to communicate with Tobii eye trackers.
* **numpy:** For efficient numerical data processing.
* **matplotlib:** For generating real-time and static gaze visualizations.
* **time:** For managing sampling rates and data timestamps.

## ⚠️ Prerequisites & Compatibility

### 1. Python Version
This project is optimized for **Python 3.10**. Using older or significantly newer versions may cause compatibility issues with the Tobii SDK.

### 2. Licensing
A valid **Tobii Pro license** is required to access data via the SDK. Please ensure your device is licensed and recognized by the *Tobii Pro Eye Tracker Manager*.

### 3. Supported Models
This library (tobii-research) officially supports the following models:
* Tobii Pro Fusion
* Tobii Pro Spectrum
* Tobii Pro Nano
* Tobii Pro Glasses 2 & 3
* Tobii TX300, T60, T120, X2-30, X2-60, X3-120

### 4. Suggestions
* Activate an environment and install python 3.10 in it and, then setup all the libraries to work the program successfully. 
