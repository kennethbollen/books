NY Times Best Seller Books with GoodReads User Ratings
======================================================
Project that investigated how book publisher's performed over the last 5-years on the New York best seller times list and comparing that with the books average user rating (provided by GoodReads.com) 

Data Extract (data_extract.py)
------------------------------
File provides code used to web scrap 5 years of data from NY times best seller list for information on book titles, book authors, publishers, best seller week and best seller rank. Additionally, utilising the GoodReads API to gather data on the average user ratings for books. Data extract requires a personal API key for Goodreads, please replace your key with the following variable:

    gr_api_key = XXX

Data Analysis (data_analysis.py)
--------------------------------
File provides code used to perform hypothesis testing on the research question of whether there is statistically significant difference between the sales performance of fiction and non-fiction books.

Exploratory Data Analysis (eda_2.py)
------------------------------------
Files provides the code used to do the initial exploratory data analysis that investigated the relationships between many of the variables
