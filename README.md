# ANLP Project Code

In this repository you can find all the coding we used in our project

 ## 1. Data Retrieving Folder

 In this folder you can find the code we used to decompress `.zst` files and save each year in a different Output `.csv` file.

 The order to run this is:
 1. In your terminal run `python3 submission_decompressor.py` changing only `input_file`, `from_date`, and `to_date` accordingly. 
 2. Go to `comment_submission_mix.ipynb` and run all the lines in there changing `comments_input` and `combined_input`.

 ## 2. IAA

 With the selection of the 1000 random datapoints, each team member annotated 1 = Kind and 0 = Not Kind. The `iaa.ipynb` calculates both Cohen's Kappa and Fleiss' Kappa.

 ## 3. Model

 This folder contained two Google Colabs, one with the BERT model and other one with the Sentence BERT. Since BERT perfomed better than our Majority Class, we trained that model to finally have the predictions. In this case, we used 600 datapoints as train, 200 as dev and 200 as test. This can be seen in the results of both models.

 ## 4. Results
 It can be found the result of our model and the trend accross time in the `test_results.ipynb` jupyter notebook.