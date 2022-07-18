# nogo count plot
no_go_count = []

for session in alldat:
  filter = (session['contrast_right'] == 0) & (session['contrast_left'] == 0)
  no_go_count.append(np.sum(filter))

plt.title('Number of NoGo trials in each session')
plt.xlabel('Session index')
plt.ylabel('Count')
plt.stem(no_go_count)
plt.show()

# ___________________________________________________________________________________

# nogo percentage plot
no_go_percentage = []

for session in alldat:
  filter = (session['contrast_right'] == 0) & (session['contrast_left'] == 0)
  no_go_percentage.append(np.mean(filter)*100)

plt.title('Percentage of NoGo trials in each session')
plt.xlabel('Session index')
plt.ylabel('Percentage')
plt.stem(no_go_percentage)
plt.show()
