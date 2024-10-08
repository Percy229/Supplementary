# Algorithm Description
## Overview
The aim of this study was to encode GIF files into DNA sequences using a voxel-based encoding strategy. Each pixel was assigned one of the four DNA bases based on its color, while preserving the XY coordinates on the image. DNA sequences were then generated from the GIF information in sequential frames. These sequences were subsequently compared against a randomly generated library containing 1,000 sequences, each 120 nucleotides in length. The number of matched sequences is used to evaluate the feasibility and applicability of the method in practical applications
## 1. System Requirements
### Software dependencies:
- **Python (version 3.7 or higher)**
- Required Python packages:
  - `Pillow` 
  - `numpy` 
  - `pandas` 
- **Operating Systems**:  
  - Windows 10 and 11
  - macOS 10.15
  - Linux (Ubuntu 20.04)

### Tested on:
- Windows 10, Windows 11, macOS 10.15, and Ubuntu 20.04 with Python 3.7 and Python 3.12

### Hardware requirements:
- No non-standard hardware required
- Minimum 4GB RAM and 100MB free disk space

## 2. Installation Guide
1. **Clone the repository**:

    ```bash
    git clone https://github.com/Percy229/Supplementary.git
    ```

2. **Navigate to the project folder**:

    ```bash
    cd src
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Estimated installation time**:

    On a standard desktop computer, installation should take approximately 1-3 minutes.

## 3. Demo
### Running the Demo:

1. **Input**:  
   Place your GIF file in the `input/` directory.

2. **Run the code**:

    ```bash
    python convert_gif_to_atcg.py --input input/sample.gif --output output/converted_atcg.csv
    ```

3. **Expected output**:  
   Comparison results of the converted ATCG sequence with sequences in randomly generated DNA pool will be saved in `output/converted_atcg.csv`.

4. **Expected run time**:  
   On a standard desktop computer, processing a 1MB GIF takes approximately 5-10 seconds.

## 4. Instructions for Use

### How to run on your data:

1. Place your GIF file in the `input/` folder or provide the path in the command line.

2. Run the following command to convert your GIF to get the comparison results of the converted ATCG sequence with sequences in randomly generated DNA pool:

    ```bash
    python convert_gif_to_atcg.py --input <path_to_your_gif> --output <path_to_output_file>
    ```
