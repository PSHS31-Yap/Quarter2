#===========================================
#       Programmer : Brentt Ethann R. Yap
#       Date       : 11/24/26
#==========================================
score = []

for i in range(0,5):
    scores = int(input(f"Enter Quiz {i+1} Score: "))
    score.append(scores)


number_of_quiz = len(score)
total_score = sum(score)
average_score = total_score / number_of_quiz
highest_score = max(score)
lowest_score = min(score)
ascending = score.copy()
ascending.sort()
descending = ascending.copy()
descending.reverse()


print("========== QUIZ SCORE REPORT =========")
print(f"Quiz Scores:    {score}")
print(f"Number of quizzes: {number_of_quiz}")
print(f"Total score: {total_score}")
print(f"Average score: {average_score:.2f}")
print(f"Highest score: {highest_score}")
print(f"Lowest score: {lowest_score}")
print(f"Ascending score: {ascending}")
print(f"Descending score: {descending}")
print(f"Original Score: {score}")
print("=======================================")