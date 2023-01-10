# Analysis of students dropout and academic success

I will be analyzing dataset created from a higher education institution (acquired from several disjoint databases) related to students enrolled in different undergraduate degrees, such as agronomy, design, education, nursing, journalism, management, social service, and technologies.

The dataset includes information known at the time of student enrollment (academic path, demographics, and social-economic factors) and the students' academic performance at the end of the first and second semesters.

The dataset is available in [this link](https://zenodo.org/record/5777340#.Y7FJotJBwUE), and the paper is available in [this link](https://www.mdpi.com/2306-5729/7/11/146)

I didn't read the paper before doing the analysis, I didn't want my analysis to be biased by the conclusions of the paper. At the end, I will be doing a comparison between my conclusions and theirs.

In the dataset, all the categorical columns are encoded as numeric. The original categories are not easily available in a file, but we can scrap them from [this website](https://valoriza.ipportalegre.pt/piaes/features-info-stats.html), this is done in the *web_scraper.ipynb* notebook, and the result is the *categorical_maps.pkl* file.
