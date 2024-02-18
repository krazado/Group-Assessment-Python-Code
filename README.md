## Executive summary/ abstract 
Companion's Breweries must choose between acquiring Site A, a countryside family pub, or Site B, a disused inner-city church, to expand its pub network. A regression model, using data from 47 existing pubs, predicts revenue based on factors like Management Quality, Staff Quality, Interior Type, Regional Income, and Competition Density. Site A's projected revenue ranges from £7.12 to £10.64 million, while Site B's range is £2.02 to £5.55 million. Despite Site B's potential for premium pricing and long-term growth, Site A is recommended for its safer investment profile, established operation, and loyal staff. Further due diligence on Site A's repair costs and revenue potential is advised, while Site B may be suitable for a longer-term, ambitious project.
## Intruduction 
Companion's Breweries faces a pivotal decision on expanding its operations. This report evaluates two prospective sites, leveraging data from 47 existing pubs, to inform investment decisions. Site A, a profitable countryside pub, and Site B, a unique inner-city church conversion, present distinct opportunities and challenges. Recommendations will consider market dynamics, strategic goals, and revenue/cost analysis. Our goal is to equip Companion's Breweries with actionable insights for informed decision-making.
## Methodology
Due to the significant correlation observed between Staff Quality (STA) and Management Quality (MAN), and the strong fit of the MAN variable within the model, it was deemed appropriate to exclude the STA variable from subsequent analysis to prevent multicollinearity issues. Regarding the Competition (COM) variable, various non-linear models including X^2, Log(x), and 1/X were initially tested to explore potential relationships. However, despite these efforts, no clear pattern or relationship between COM and Revenue (REV) was discerned from the data.

# Step-by-Step Analysis Process: Evaluating Variables and Model Fit in Linear Regression
## Step 0 : We run correlation Analysis
   ![alt text](resources/correlation_matrix.png)
   
   From this matrix, it is clear that we have a very strong correlation between MAN and STA, which can be a significant problem in our multiple linear regression. However, we still apply it to observe that assumption.
## Step 1 : We run multi Linear Regression Analysis
   ![alt text](resources/linear_regression_step1.png)
    
   After eyeballing the results, it is clear that the p-values for COM and SAT are out of control, meaning that this regression model is not what we are looking for.
## Step 2 : We exlude SAT From Independent Variables And Run multi Linear Regression Analysis
   ![alt text](resources/linear_regression_step2.png)
   
   Even if there's a strong relationship between the dependent variable (REV) and an independent variable (MAN), it's crucial to assess for multicollinearity, which occurs when independent variables are highly correlated with each other. This can inflate standard errors and make coefficient estimates unstable, this is not a case here!
   Instead what we see is that COM is still destorying model, since we see that there is almost no correlation to the target variable, we will exclude it from the model.
## Step 3 : We exlude COM From Independent Variables And Run multi Linear Regression Analysis   
   ![alt text](resources/linear_regression_step3.png)
   
   Finally, we have obtained a model that appears quite satisfactory, with an Adjusted R-squared value of 95% and statistically significant p-values
## Step 4 : After excluding the COM variable, we observe that the model is a good fit. However, we cannot stop here; we must examine if there is a non-linear relationship
   ![alt text](resources/com_variable_non_linearscatter.png)

