# Unsupervised Learning and Feature Engineering
This repository is a project for my studies at IU for the course: ML - Unsupervised Learning and Feature Engineering. 
The project investigates the current topics in science. For this purpose the arXiv Dataset from [Kaggle](https://www.kaggle.com/datasets/Cornell-University/arxiv) was chosen and the most important terms were extracted. The results were then visualized with different approaches.

Due to github's restrictions of datasize, the used dataset can't be uploaded to this repository. The used version is *110* and can be retrieved from [this page](https://www.kaggle.com/datasets/1b6883fb66c5e7f67c697c2547022cc04c9ee98c3742f9a4d6c671b4f4eda591/versions/110).

### Preparing the environment

For stable usage of the application, **python version 3.9.15** is recommended. Install python from the [official website](https://www.python.org/). Check your python version with entering your command promt and execute the following command:

```python
python --version 
```

It is recommended to use a customized environment to ensure full functionality, e.g. with the distribution anaconda, which can be downloaded [here](https://www.anaconda.com/products/distribution).

Install the required packages with the following command in your command line interface (For more information about pip, please check the [pip documentation](https://pip.pypa.io/en/latest/user_guide/)):

```python
pip install -r requirements.txt 
```

Since no configuration was found in which both libraries, **yellowbrick** and **pyLDAvis**, worked, two *requirements.txt* are provided. Please consider this when installing the libraries. 

If you choose to use the *requirements.txt* for **pyLDAvis**, you'll have to interchange the *get_feature_names_out()* functions of scikit-learn to *get_feature_names()*. The results from pyLDAvis can also be retrieved from *model/lda.html*.


&nbsp;


## Structure of the Repo:
The feature selection part, where the most recent data is retrieved, is conducted in the file *feature_selection.py*. 
All following implementations are stored in the file *main_notebook.ipynb*.
The folder *pics* contains the pictures created in this repository, including the Silhouette Scores. 
The folder *data* simple contains the link to the used dataset due to storage restriction.
The folder *model* contains some results of the models, including the html file for pyLDAvis.
