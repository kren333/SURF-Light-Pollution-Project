library(car)
LP_PLUS_DEMOGRAPHICS <- read.csv("Downloads/LP_DATA.csv", header=TRUE, stringsAsFactors=FALSE)

# Generate Correlation Matrix

corr_data <- LP_PLUS_DEMOGRAPHICS[, c("Modified.Averages", "Total.Population", "Unemployment.Rate", "Percentage.of.Household.w.SNAP.or.Public.Assistance.Income")]
cor_matrix <- cor(corr_data, method = "spearman")
round(cor_matrix, 2)

# Rename Variables

LP <- LP_PLUS_DEMOGRAPHICS$Modified.Averages
unemployment_rate <- LP_PLUS_DEMOGRAPHICS$Unemployment.Rate
population <- LP_PLUS_DEMOGRAPHICS$Total.Population
snap_pc <- LP_PLUS_DEMOGRAPHICS$Percentage.of.Household.w.SNAP.or.Public.Assistance.Income

# Histograms of All Variables

hist(LP)
hist(unemployment_rate)
hist(population)
hist(snap_pc)

# Series of Scatter Plots

plot(LP~unemployment_rate , ylim = rev(range(LP)) ,
     bty="n" , xlab = "Unemployment Rate", ylab="Light Pollution Values")
title("Scatter Plot of Light Pollution v. Unemployment Rate") 

abline(unemployment_model,col='red')


plot(LP~population , ylim = rev(range(LP)) ,
     bty="n" , xlab = "Population", ylab="Light Pollution Values")
title("Scatter Plot of Light Pollution v. Population") 

plot(LP~snap_pc , ylim = rev(range(LP)) ,
     bty="n" , xlab = "Percentage of Population Recieving SNAP or Public Assistance Income", ylab="Light Pollution Values")
title("Scatter Plot of Light Pollution v. Public Assistance Proportion") 

# Confirm that population/unemployment aren't super visually correlated so that multicollinearity isn't an issue for multivariate linear regression

plot(population~unemployment_rate ,
     bty="n" , xlab = "Unemployment Rate", ylab="Population")
title("Scatter Plot of Population v. Unemployment Rate")

# Build/present multivariate linear regression predicting LP

all_var_model <- lm(Modified.Averages ~ Total.Population + Unemployment.Rate + Percentage.of.Household.w.SNAP.or.Public.Assistance.Income, data=LP_PLUS_DEMOGRAPHICS)
vif(all_var_model)
summary(all_var_model)

bivar_model <- lm(Modified.Averages ~ Total.Population + Unemployment.Rate, data=LP_PLUS_DEMOGRAPHICS)
vif(bivar_model)
summary(bivar_model)

unemployment_model <- lm(Modified.Averages ~ Unemployment.Rate, data=LP_PLUS_DEMOGRAPHICS)
summary(unemployment_model)



