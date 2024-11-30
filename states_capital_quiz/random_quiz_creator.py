#!/usr/bin/env python3

import random
# remove this comment if running on Windows - from pathlib import Path

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

number = 0
for quizNum in range(35):

    states = []
    capitals_list = []
    answer_list = []
    number += 1
    question_number = 0
    answer_number = 0
    quiz_name = f"/home/gonzo185/projects/random_quiz_project/created_quizes/Random_Quize_Pojectcapitalsquiz{number}_modified.txt"

    quiz = open(f'{quiz_name}', 'w',)

    quiz.write(f"Name:\n\nDate:\n\nPeriod:\n\n\t\t\tState Capitals Quiz (Form {number})\n\n")

    for state in capitals.keys():
        states.append(state)
    random.shuffle(states)

    for capital in capitals.values():
        capitals_list.append(capital)
    random.shuffle(capitals_list)

    for state in states:
        question_number += 1
        answer = capitals.get(state)
        multiple_choice = [answer]
        random.shuffle(capitals_list)
        while len(multiple_choice) < 4:
            for capital in capitals_list[:3]:
                if capital == answer:
                    continue
                else:
                    multiple_choice.append(capital)
        random.shuffle(multiple_choice)

        if answer == multiple_choice[0]:
            correct_answer = "A"
        elif answer == multiple_choice[1]:
            correct_answer = "B"
        elif answer == multiple_choice[2]:
            correct_answer = "C"
        elif answer == multiple_choice[3]:
            correct_answer = "D"
        answer_list.append(correct_answer)

        quiz = open(f'{quiz_name}', 'a')
        quiz.write(f"\n\n{question_number}. What is the capital of {state}?\nA. {multiple_choice[0]}\nB. {multiple_choice[1]}\nC. {multiple_choice[2]}\nD. {multiple_choice[3]}")
    quiz.write("\n\n------------------------------------------------\n\n")
    for correct_answer in answer_list:
        answer_number += 1
        quiz.write(f"{answer_number}. {correct_answer}\n")
    quiz.close()
print("done")
