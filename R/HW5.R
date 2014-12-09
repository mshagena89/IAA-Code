#Solutions for Data Mining HW5

#variance-covariance Matrix
sigma = matrix(c(100, -40, -40, 25), nrow=2, ncol=2)

#calculate sigma inverse, used later in mahalanobis function
sigmaInv = solve(sigma)

#calculating Euclidean Distance between individual and Means

#distance between individual and non-defaulter
nondef <- matrix(c(5,5,8,8), nrow=2,ncol=2, byrow=TRUE)
dist(nondef, method="euclidean")

#non defaulter distance = 4.24 

#distance between individual and defaulter
defaulter <- matrix(c(5,5,15,6), nrow=2,ncol=2, byrow=TRUE)
dist(defaulter, method="euclidean")

#defaulter distance = 10.04988

#looks like a non-defaulter, based on euclidean distance!

#mahalanobis distance calculations
individual <- matrix(c(8,8), nrow=1)
defaulterMean <- matrix(c(15,6), nrow=1)
nonDefMean <- matrix(c(5,5), nrow=1)

#calculate mahalanobis for Individual and Defaulter Mean
mahalanobis(individual, defaulterMean, sigmaInv, inverted=TRUE)
#.0561111

#calculate mahalanobis for Individual and non-Defaulter Mean
mahalanobis(individual, nonDefMean, sigmaInv, inverted=TRUE)
#2.05

#Based on Mahalanobis Distance, Individual is more likely to be a defaulter!

