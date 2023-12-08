from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton, QComboBox, QPushButton
import sys
import logic


class Gui(QWidget):
    def __init__(self, parent=None):
        '''
        Initialize the GUI with a given Qt window
        :param parent: The parent QWidget (default is None)
        '''
        super().__init__(parent)
        self.allow_voting = False  # New state variable

        # Radio Buttons
        self.layout = QVBoxLayout(self)
        self.label_operation = QLabel('Options\t', self)
        self.label_operation.setGeometry(20, 20, 62, 21)
        self.radio_1 = QRadioButton('Vote', self)
        self.radio_2 = QRadioButton('Exit', self)

        # Set fixed positions for radio_1 and radio_2
        self.radio_1.setGeometry(20, 40, 62, 21)
        self.radio_2.setGeometry(20, 80, 62, 21)

        self.radio_1.toggled.connect(self.option)
        self.radio_2.toggled.connect(self.option)
        self.layout.addWidget(self.label_operation)
        self.layout.addWidget(self.radio_1)
        self.layout.addWidget(self.radio_2)

        # Initialize other UI components here without changing their positions
        # self.label_candidate_name = QLabel('Names\t', self)
        # self.combo_box_names = QComboBox(self)
        # self.combo_box_names.addItem('Cameron')
        # self.combo_box_names.addItem('Allison')
        # self.combo_box_names.addItem('Diego')
        # self.layout.addWidget(self.label_candidate_name)
        # self.layout.addWidget(self.combo_box_names)
        #
        # # Results label
        # self.label_result = QLabel(self)
        # self.layout.addWidget(self.label_result)
        # self.label_result.setText('')
        #
        # # Vote Button
        # self.enter_button = QPushButton('VOTE', self)
        # self.enter_button.clicked.connect(self.compute)
        # self.layout.addWidget(self.enter_button)

    def option(self):
        '''
        Handle the user's selection of options using radio buttons.
        '''
        if self.radio_1.isChecked():
            self.allow_voting = True  # Allow voting when the user selects 'Vote'
            self.label_candidate_name = QLabel('Names\t', self)
            self.combo_box_names = QComboBox(self)
            self.combo_box_names.addItem('Cameron')
            self.combo_box_names.addItem('Allison')
            self.combo_box_names.addItem('Diego')
            self.layout.addWidget(self.label_candidate_name)
            self.layout.addWidget(self.combo_box_names)

            # Results label
            self.label_result = QLabel(self)
            self.layout.addWidget(self.label_result)
            self.label_result.setText('')

            # Vote Button
            self.enter_button = QPushButton('VOTE', self)
            self.enter_button.clicked.connect(self.compute)
            self.layout.addWidget(self.enter_button)

            # # Results label
            # self.label_result.setText('')

        elif self.radio_2.isChecked():
            self.allow_voting = False  # Disallow voting when the user selects 'Exit'
            self.label_candidate_name.setText('')  # Clear candidate names
            self.combo_box_names.hide()

            # Clear results
            self.label_result.setText('')

    def compute(self):
        '''
        Perform the computation based on the user's voting selection.
        '''
        if not self.allow_voting:
            return  # Don't allow voting when the program is in 'Exit' mode

        selected_candidate_index = self.combo_box_names.currentIndex()

        if selected_candidate_index in (0, 1, 2):
            # Create an instance of VotingLogic
            voting_logic = logic.VotingLogic()
            # Vote for the selected candidate
            voting_logic.vote(selected_candidate_index)

            # Display the results
            results = voting_logic.get_results()
            formatted_results = '\n'.join(results)
            self.label_result.setText(formatted_results)

        else:
            self.label_result.setText('No options selected')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Gui()
    window.setWindowTitle('Voting Menu')
    window.setGeometry(100, 100, 400, 230)
    window.show()
    sys.exit(app.exec())
