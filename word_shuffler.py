import random


def get_key(user_dict: dict, value: any) -> any:
    """
    :param: user_dict: input dictionary
    :param: value: value of dictionary
    :return: key for value
    """
    for k, v in user_dict.items():
        if v == value:
            return k


def shuffle_words(filename: any) -> dict:
    """
    :param: filename: is a file which contains english words, each on a different line
    1.getting a list of lines in file without \n; 2.shuffling them and appending to another list;
    :return: returns a list of values of shuffled words, got from a filename
    """
    with open(filename) as opened_file:
        lines = [line.rstrip() for line in opened_file]
        shuffled_lines = {}
        for word in lines:
            shuffled_lines.update({word: ''.join(random.sample(word, len(word)))})
        return shuffled_lines


def write_history(history_list: list, filename: any):
    """
    :param: filename: is a file, which we open to write top players in it and their stats
    :param: history_list: list with a username and points
    :return: returns our output to file
    """
    with open(filename, 'a') as history_file:
        history_file.write(f'{":".join(history_list)}\n')
    # return: idk what to return from this function, it would be great for some commentary


def get_statistics(filename: any, username: str) -> str:
    """
    :param filename: input historical file for getting stats
    :param username: getting stats for defined username
    :return: count of lines with exact user and maximum points for him
    """
    counts = 0
    extremum = []
    with open(filename) as statistics_file:
        for line in statistics_file.readlines():
            if username == line.partition(':')[0]:
                counts += 1
                extremum.append(int(line.partition(':')[2].rstrip()))
    return f'Total games: {counts}, record: {max(extremum)}'


def main():
    shuffled_list = shuffle_words("english_words.txt")
    iteration = 0
    points_counter = 0
    points_iteration = 10

    question_list = []
    for value in shuffled_list.values():
        question_list.append(value)

    user_greetings = input('Enter your name: ')

    # # loop for answering and getting some points
    while iteration < 5:
        iteration += 1
        question = random.choice(question_list)
        print(f'Guess the word: {question}')
        answer = input('My answer is: ')
        if answer == get_key(shuffled_list, question):
            print(f'Correct! You have got {points_iteration} points!')
            points_counter += points_iteration
        else:
            print(f'Wrong! Correct answer is {get_key(shuffled_list, question)}')

    # writing history in the historical file
    score = [user_greetings, str(points_counter)]
    write_history(score, 'history.txt')

    # getting statistics
    print()
    print(get_statistics('history.txt', user_greetings))


main()
