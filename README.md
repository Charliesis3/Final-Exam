# Final-Exam

(a)
The coefficient of variation is a useful metric for assessing and comparing variations between different datasets. 
It is calculated by dividing the standard deviation by the mean and multiplying the result by 100, yielding a percentage. 
This measure effectively captures the spread of a dataset, making it applicable for comparing data with different units or scales. 
Additionally, the coefficient of variation serves as a valuable tool for evaluating the stability of variables or scales within a dataset.

(b)
Among the four regions, price fluctuations exhibit the highest average ranging from 56.6 to 33.3. When ranked in descending order 
based on average, the South region takes the lead, followed by the Northeast, Midwest, and lastly the West with the lowest average. 
Considering the coefficient variable, the West region demonstrates the most favorable price variations, 
while the Northeast region shows the least favorable.

(c)
+--------------------------------------------------+-------------------------------------+------------------------------------------+
| Functionality                                    | In R                                | In Python                                |
+--------------------------------------------------+-------------------------------------+------------------------------------------+
| Merge data                                       | merge()                             | pd.merge()                               |
+--------------------------------------------------+-------------------------------------+------------------------------------------+
| Remove Washington DC                             | gp_ByRegion %>% filter(Code !="DC") | gp_ByRegion[gp_ByRegion['Code'] != 'DC'] |
+--------------------------------------------------+-------------------------------------+------------------------------------------+
| Group by region and calculate percent increase,  | group_by(Region) %>%                | groupby(['Region']).agg                  |
| standard deviation, and coefficient of variation | summarise                           |                                          |
+--------------------------------------------------+-------------------------------------+------------------------------------------+
| Read in the data                                 | read.csv                            | pd.read_csv                              |
+--------------------------------------------------+-------------------------------------+------------------------------------------+

(d)
My Favorite topic/assigment that we did this year was the guess the number assigment. I thought it was super cool how we could create a code and then interact with it. I enjoyed being able to guess the number and play the game myself. I enjoyed messing around with the for(), if() elif() else(), while() functions.
