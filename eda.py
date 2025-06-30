import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('dataset/Students_gamification_grades.csv')

# Print dataset head
print('Dataset Head:')
print(df.head())

# Print dataset info
print('\nDataset Info:')
df.info()

# Print dataset description
print('\nDataset Description:')
print(df.describe())

# Handling missing values in Practice_Exam by filling with the mean
df["Practice_Exam"].fillna(df["Practice_Exam"].mean(), inplace=True)

# Print dataset info after handling missing values
print("\nDataset Info after handling missing values:")
df.info()

# Comparative analysis: Users vs. Non-Users
user_data = df[df["User"] == 1]
non_user_data = df[df["User"] == 0]

# Print comparative analysis
print("\n--- Comparative Analysis (Users vs. Non-Users) ---")
print("\nMean Final Exam Grade:")
print(f'Users: {user_data["Final_Exam"].mean():.2f}')
print(f'Non-Users: {non_user_data["Final_Exam"].mean():.2f}')

print("\nMean Practice Exam Grade:")
print(f'Users: {user_data["Practice_Exam"].mean():.2f}')
print(f'Non-Users: {non_user_data["Practice_Exam"].mean():.2f}')

print("\nMean Average Grade for Quizzes (Users only):")
for i in range(1, 7):
    print(f"Q{i}: {user_data[f'Avg_Grade_Q{i}'].mean():.2f}")

print("\nMean Number of Accesses for Quizzes (Users only):")
for i in range(1, 7):
    print(f"Q{i}: {user_data[f'No_access_Q{i}'].mean():.2f}")

# Correlation Analysis
print("\n--- Correlation Analysis ---")
correlation_matrix = df.corr(numeric_only=True)
print("Correlation Matrix (selected columns):")
print(correlation_matrix[["User", "Final_Exam", "Practice_Exam"]].loc[["User", "Final_Exam", "Practice_Exam", "Avg_Grade_Q1", "Avg_Grade_Q2", "Avg_Grade_Q3", "Avg_Grade_Q4", "Avg_Grade_Q5", "Avg_Grade_Q6", "No_access_Q1", "No_access_Q2", "No_access_Q3", "No_access_Q4", "No_access_Q5", "No_access_Q6"]])

# Visualizations

# Distribution of Final Exam Grades
plt.figure(figsize=(10, 6))
sns.histplot(df["Final_Exam"], kde=True)
plt.title("Distribution of Final Exam Grades")
plt.xlabel("Final Exam Grade")
plt.ylabel("Frequency")
plt.savefig("final_exam_distribution.png")
plt.close()

# Final Exam Grades: Users vs. Non-Users
plt.figure(figsize=(10, 6))
sns.boxplot(x="User", y="Final_Exam", data=df)
plt.title("Final Exam Grades: Users vs. Non-Users")
plt.xlabel("User (0=Non-User, 1=User)")
plt.ylabel("Final Exam Grade")
plt.savefig("final_exam_users_vs_nonusers.png")
plt.close()

# Average Grades for Quizzes (Users only)
quiz_grades = user_data[["Avg_Grade_Q1", "Avg_Grade_Q2", "Avg_Grade_Q3", "Avg_Grade_Q4", "Avg_Grade_Q5", "Avg_Grade_Q6"]].mean()
plt.figure(figsize=(10, 6))
sns.barplot(x=quiz_grades.index, y=quiz_grades.values)
plt.title("Average Grades for Quizzes (Users only)")
plt.xlabel("Quiz")
plt.ylabel("Average Grade")
plt.savefig("avg_quiz_grades_users.png")
plt.close()

# Number of Accesses for Quizzes (Users only)
quiz_accesses = user_data[["No_access_Q1", "No_access_Q2", "No_access_Q3", "No_access_Q4", "No_access_Q5", "No_access_Q6"]].mean()
plt.figure(figsize=(10, 6))
sns.barplot(x=quiz_accesses.index, y=quiz_accesses.values)
plt.title("Average Number of Accesses for Quizzes (Users only)")
plt.xlabel("Quiz")
plt.ylabel("Average Number of Accesses")
plt.savefig("avg_quiz_accesses_users.png")
plt.close()

print("Visualizations saved as PNG files.")
