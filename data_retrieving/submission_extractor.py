import csv
def extract_author_id(csv_file):
    submission_info_dict = {}

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            prefix_id = ('t3_'+str(row[2]))

            # title, subreddit, id, author, body - and we need only title, body, subreddit, and author to be mapped to an id
            submission_info_dict[prefix_id] = [row[0], row[4], row[1], row[3]]

    return submission_info_dict


