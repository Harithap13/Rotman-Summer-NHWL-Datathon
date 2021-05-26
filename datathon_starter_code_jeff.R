#Exercise: Building a shot prediction model in hockey

#STEP 1#
#read in the data and convert it to a dataframe
shot_data=read.csv("/Users/jeff_/Desktop/Rotman MMA Summer Datathon (men&women olympic).csv",T)
shot_data <- data.frame(shot_data)


#STEP 2#
#filtering the dataset for shots only, adding a variable for goal scored or not#
shot_data <- shot_data[shot_data$event_type == 'Shot', ]


#STEP 3#
#creating a variable for if a goal was scored or not#
shot_data$goal <- ifelse(shot_data$event_successful == 't', 1, 0)


#STEP 4#
#build the predictive model using logistic regression from the GLM package
shot_model <- glm(shot_data$goal ~ shot_data$x_event + shot_data$y_event + shot_data$shot_type 
           , data = shot_data, family = "binomial")
summary(shot_model)

#STEP 5#
#make predictions and output csv#
shot_data$goal_predictions <- predict(shot_model, shot_data,type = "response")
write.csv(shot_data,file='/Users/jeff_/Desktop/shot_model_output.csv')

