from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """
        Initialize the Logic class.

        This class inherits from QMainWindow and sets up the UI using the setupUi method.

        """
        super().__init__()
        self.setupUi(self)
        self.__candidate_cbox = self.candidate_comboBox
        self.summary_label.setWordWrap(True)
        self.vote_radiobtn.clicked.connect(lambda: self.candidates_display())
        self.vote_button.clicked.connect(lambda: self.vote(self.__candidate_cbox))
        # self.exit_radiobtn.clicked.connect(lambda: self.vote(self.__candidate_cbox))

    def candidates_display(self):
        """
        Enable widgets for candidate selection.

        This method is connected to the vote_radiobtn and enables the candidate combo box, candidates label,
        vote button, and summary label.

        """
        self.__candidate_cbox.setEnabled(True)
        self.candidates_label.setEnabled(True)
        self.vote_button.setEnabled(True)
        self.summary_label.setEnabled(True)

    def vote(self, candidate):
        """
        Register a vote for the specific candidate and update the count on the GUI.

        :param candidate: Name of the candidate to vote for.
        """
        self.title_label.setText('')
        candidate_text = candidate.currentText()
        if self.vote_button.clicked:  # Corrected the function call
            candidates = {'Allison', 'Cameron', 'Sam', 'Diego'}
            if candidate_text in candidates:
                # Assuming vote_counts is an instance attribute
                if not hasattr(self, 'vote_counts'):
                    self.vote_counts = {'Allison': 0, 'Cameron': 0, 'Sam': 0, 'Diego': 0}

                # Increment the vote for the chosen candidate
                self.vote_counts[candidate_text] += 1

                # Display the updated summary
                summary_text = ""
                for candidate_text, vote_count in self.vote_counts.items():
                    summary_text += f"{candidate_text}: {vote_count}\n"

                self.summary_label.setText(summary_text)

                # Disable other widgets
                self.__candidate_cbox.setEnabled(False)
                self.candidates_label.setEnabled(False)
                self.vote_button.setEnabled(False)
                self.summary_label.setEnabled(True)

        elif self.exit_radiobtn.clicked:
            self.vote_counts = {'Allison': 0, 'Cameron': 0, 'Sam': 0, 'Diego': 0}
            return self.title_label.pyqtConfigure(text='Summary')
