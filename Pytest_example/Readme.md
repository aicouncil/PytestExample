## Pytest

"In MLOps, we deal with pipelines, models, APIs, and complex workflows. If any step in this pipeline fails, it can disrupt the entire process. For instance:

    * A data preprocessing script might generate incorrect outputs due to faulty logic.
    * A machine learning model’s predictions might be misaligned because of a change in the data format.

To catch these issues, we use testing frameworks like pytest, which are lightweight, flexible, and easy to integrate."

# Why Testing is Critical in MLOps:

    * In MLOps, continuous integration and deployment (CI/CD) pipelines are the backbone. Automated testing ensures that:
        * Every change in the codebase is validated.
        * New features or updates don’t break existing functionality.
        * Models and scripts produce accurate results after deployment.

# Example in MLOps:

    * Imagine you’re deploying a model API that predicts house prices.
        * What if your API fails to handle negative values?
        * Or the preprocessing step mistakenly normalizes categorical data?
        With pytest, you can write test cases to catch such issues.


calculator/
├── main.py
├── test_add.py
└── setup.py
