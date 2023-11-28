

## Essential Statistics for Data Science

Welcome to "Essential Statistics for Data Science" – a collection of notes on fundamental statistics for experimental sciences and data science enthusiasts. These notes are particularly beneficial for those embarking on a career in data science. The content of these notes has evolved through teaching, discussions, and supervision of experiments.

## Books Used

The following four books have been extensively referenced and used during the creation of these lecture notes:

1. **Introductory Statistics**
   - Author: S. M. Ross
   - Year: 2017
   - Publisher: Academic Press

2. **Introduction to Probability and Statistics for Engineers and Scientists**
   - Author: S. M. Ross
   - Year: 2020
   - Publisher: Academic Press

3. **Probability and Statistics for Engineers and Scientists**
   - Authors: R. E. Walpole, R. H. Myers, S. L. Myers, K. Ye
   - Year: 1993
   - Publisher: Macmillan New York

4. **Introductory Statistics**
   - Authors: N. A. Weiss, C. A. Weiss
   - Year: 2017
   - Publisher: Pearson London

## Workflow Details

The workflow consists of the following steps:

1. **Set up Git repository**: This step checks out the repository on the GitHub Actions runner.

2. **Compile LaTeX document**: The LaTeX document (specified as `main.tex` in the workflow) is compiled into a PDF using the [GitHub Action for LaTeX](https://github.com/xu-cheng/latex-action). The resulting PDF is then saved as an artifact.

3. **Upload PDF file**: The compiled PDF file is uploaded as an artifact, making it accessible for further use or manual download.

## Usage
## LaTeX to PDF Conversion with GitHub Actions

This repository includes an automated workflow that converts a LaTeX document to a PDF using GitHub Actions. The workflow is triggered on each push to the main branch, ensuring that the PDF is always up-to-date with the latest changes to the LaTeX document.

To compile the LaTeX document and generate the PDF locally, you can follow these steps:

1. Clone the repository:

   ```bash
   git clone [repository-url]
2. cd [EssentialStatistics]
