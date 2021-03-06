import config
tee = config.Tee('../Results/%s/CNB_GroupAC%s%s_model.txt' % (config.args.dataset, config.args.tf_idf, config.args.remove_non), 'w')
from header_model_data import *
from sklearn.naive_bayes import ComplementNB

print("Regrouping the labels")
for i in range(len(yDF)):
    if(yDF[i] == pr.y_conversion('challenge')):
        yDF[i] = pr.y_conversion('agree')
 
print("The Class Distribution is:")
classDist = Counter(yDF)
for k in classDist.keys():
    print("\t"+str(pr.conversion_y(k))+":"+str(classDist[k]))

print("Defining and doing a Complement Naive Bayes classifier")

NB = ComplementNB()
scores = cross_validate(NB, xDF, yDF, cv=logo, scoring = scorer)

#print(scores)
#print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
compute_stats(originalclass, predictedclass, True)
print("Confusion Matrix")

labelList = [x for x in classDist.keys()]


print_cm(confusion_matrix(originalclass, predictedclass, labels = labelList), [pr.conversion_y(x) for x in labelList])

tee.close()
