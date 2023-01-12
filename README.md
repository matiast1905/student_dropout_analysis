# Analysis of students dropout and academic success

I will be analyzing dataset created from a higher education institution (acquired from several disjoint databases) related to students enrolled in different undergraduate degrees, such as agronomy, design, education, nursing, journalism, management, social service, and technologies.

The dataset includes information known at the time of student enrollment (academic path, demographics, and social-economic factors) and the students' academic performance at the end of the first and second semesters.

The dataset is available in [this link](https://zenodo.org/record/5777340#.Y7FJotJBwUE), and the paper is available in [this link](https://www.mdpi.com/2306-5729/7/11/146)

I didn't read the paper before doing the analysis, I didn't want my analysis to be biased by the conclusions of the paper. At the end, I will be doing a comparison between my conclusions and theirs.

In the dataset, all the categorical columns are encoded as numeric. The original categories are not easily available in a file, but we can scrap them from [this website](https://valoriza.ipportalegre.pt/piaes/features-info-stats.html), this is done in the *web_scraper.ipynb* notebook, and the result is the *categorical_maps.pkl* file.

This descriptor presents a dataset created from a higher education institution (acquired from several disjoint databases) related to students enrolled in different undergraduate degrees, such as agronomy, design, education, nursing, journalism, management, social service, and technologies. The dataset includes demographic data, socioeconomic and macroeconomic data, data at the time of student enrollment, and data at the end of the first and second semesters. The data sources used consist of internal and external data from the institution and include data from (i) the Academic Management System (AMS) of the institution, (ii) the Support System for the Teaching Activity of the institution (developed internally and called PAE), (iii) the annual data from the General Directorate of Higher Education (DGES) regarding admission through the National Competition for Access to Higher Education (CNAES), and (iv) the Contemporary Portugal Database (PORDATA) regarding macroeconomic data.

The data refer to records of students enrolled between the academic years 2008/2009 (after the application of the Bologna Process to higher education in Europe) to 2018/2019. These include data from 17 undergraduate degrees from different fields of knowledge, such as agronomy, design, education, nursing, journalism, management, social service, and technologies. The final dataset is available as a comma-separated values (CSV) file encoded as UTF8 and consists of 4424 records with 35 attributes and contains no missing values.
