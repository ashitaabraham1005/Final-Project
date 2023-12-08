import csv


class VotingLogic:
    def __init__(self):
        '''
        Initialize the VotingLogic object with candidates, votes, and load existing votes from a CSV file.
        '''
        self.candidates = ['Cameron', 'Allison', 'Diego']
        self.votes = [0, 0, 0]
        self.load_votes()

    def vote(self, candidate_index):
        '''
        Register a vote for the specific candidate.

        :param candidate_index: Index of the candidate to vote for.
        '''
        self.votes[candidate_index] += 1
        self.save_votes()

    def get_results(self):
        '''
        Get the voting results as a list of strings.

        :return:
        -List[str]: A list of strings representing the results for each candidate.
        '''
        results = []
        for candidate, vote_count in zip(self.candidates, self.votes):
            results.append(f'{candidate}: {vote_count}')
        return results

    def load_votes(self):
        '''
        Load existing votes from a CSV file, if available.
        '''
        try:
            with open('votes.csv', 'r') as file:
                reader = csv.reader(file)
                try:
                    self.votes = [int(vote) for vote in next(reader)]
                except StopIteration:
                    # Handle the case where the file is empty
                    pass
        except FileNotFoundError:
            # Handle the case where the file doesn't exist yet
            pass

    def save_votes(self):
        '''
        Save the current votes to a CSV file.
        '''
        with open('votes.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(map(str, self.votes))
