# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def validate_answers():
    try:
        open("answers.csv", "r")
    except FileNotFoundError:
        print("The survey has no answer.")
        sys.exit(1)


def insights_report():
    return open("insights.txt", "w")


def get_number_total_answers(f):
    with open("answers.csv", "r") as ans_file:
        num_lines = sum(1 for _ in ans_file)
        num_lines -= 1
            
    f.write(f"Total answers: {str(num_lines)}\n")


def get_listen_music(f):
    with open('answers.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        yes = 0
        no = 0
        for row in reader:
            if row['Do you enjoy listening to music?'] == "Yes":
                yes += 1
            elif row['Do you enjoy listening to music?'] == "No":
                no += 1
        
    f.write(f"Do you enjoy listening to music? Yes: {str(yes)}\n")
    f.write(f"Do you enjoy listening to music? No: {str(no)}\n")

    ### ADD MORE INSIGHTS METRICS FUNCTIONS

decadeOptions = ["80s", "90s", "90s", "00s", "60s"]

genreOptions = ["Rock", "Rock", "Hip/Hop", "Hip/Hop", "Rock"]

yesNoOptions = ["< 4hours", "> 4hours", "< 4hours", "< 4hours", " >4hours" ]

def findFrequencies(options):
  basketFrequencies = {}

  for basketOption in options:
    # print(basketOption)
    if basketOption in basketFrequencies:
      basketFrequencies[basketOption] += 1
    else:
      basketFrequencies[basketOption] = 1

  return basketFrequencies

def mostPopularChoice(choices):
    frequencies = findFrequencies(choices)

    mostPopularChoice = None
    mostPopularFrequency = None
    for choice, frequency in frequencies.items():
      if mostPopularChoice is None or frequency > mostPopularFrequency:
        mostPopularChoice = choice
        mostPopularFrequency = frequency 

    return mostPopularChoice

# print(mostPopularChoice(decadeOptions))
print(decadeOptions)
print("\n")
print(findFrequencies(decadeOptions))
# print(findFrequencies(genreOptions))
# print(findFrequencies(yesNoOptions))


def start_insights():
    validate_answers()

    f = insights_report()
    get_number_total_answers(f)
    get_listen_music(f)
    ### ADD MORE INSIGHTS METRICS FUNCTIONS CALLS

    f.close()
    print("Insights have been generated and saved at 'insights.txt' file.\n")
