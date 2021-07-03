############################### problem1 ############################
install.packages("recommenderlab")
library(recommenderlab)
install.packages("reshape2")
library(reshape2)
install.packages("reshape")
library(reshape)
#loading the dataset
game_rating_list <- read.csv("C:\\Users\\DELL\\Downloads\\game.csv",header = TRUE)
head(game_rating_list)
dim(game_rating_list)

#convert to matrix format

ratings_matrix <- as.matrix(acast(game_rating_list, game, fun.aggregate = mean))



############################# problem2 ###################
install.packages("recommenderlab")
library(recommenderlab)
#loading the dataset
entertainment <- read.csv("C:\\Users\\DELL\\Downloads\\Entertainment.csv",header = TRUE)
head(entertainment)
entertainment <- entertainment[,2:4]
head(entertainment)
dim(entertainment)
colnames(entertainment) <- c("id" , "Titles" , "Category" ,"Reviews")
#convert to matrix format
rating_matrix <- as.matrix(acast(entertainment,Category~Titles, fun.aggregate = mean))
dim(rating_matrix)

#recommenderlab realRatingMatrix format
R <- as(rating_matrix, "realRatingMatrix")

rec1 = Recommender(R, method = "UBCF") # user based collabarative filering
rec2 = Recommender(R, method = "UBCF") # item based colllabarative filtering
rec3 = Recommender(R, method ="SVD")
rec4 = Recommender(R, method = "POPULAR")
rec5 = Recommender(binarize(R,minRating=2), method="UBCF") ## binarize all 2+ rating to 1

## create n recommendations for a user
uid = "Tom and Huck (1995)"
movies <- subset(entertainment, entertainment$user==uid)
print("You have rated:")
movies
print("recommendations for you:")
prediction <- predict(rec1, R[uid], n=2) ## you may change the model here
as(prediction, "list")
prediction <- predict(rec2, R[uid], n=2) ## you may change the model here
as(prediction, "list")
prediction <- predict(rec3, R[uid], n=2) ## you may change the model here
as(prediction, "list")
prediction <- predict(rec4, R[uid], n=2) ## you may change the model here
as(prediction, "list")
prediction <- predict(rec5, R[uid], n=2) ## you may change the model here
as(prediction, "list")

















