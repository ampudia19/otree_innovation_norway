from survey_extras.views import SurveyPage

from ._builtin import Page
from .models import Player, Constants, Subsession
from utils import *

doc = """
    Documentation
"""

class Assessment(Page, SurveyPage):
    form_model = 'player'
    form_fields = [f.name for f in Player._meta.fields if f.name.startswith('app_')]

    def vars_for_template(self):
        # Define the alphabetic label for the round
        round_label = self.participant.vars["case_rounds"][self.player.round_number]

        # Pass treatment binary
        round_show_treatment = self.participant.vars["treatment"][round_label]

        # Pass ML outputs specific to the alphabetic label
        round_ML_outputs = parse_ml_outputs(round_label)

        # Pass data selection based on case
        round_dict = parse_inputs(round_label)
        round_dict.update({
            "include_title": False,
            "app_con_field_women": [x for x in self.form_fields if "women" in x][0],
            "app_con_field_environment": [x for x in self.form_fields if "environment" in x][0],
            "app_con_field_society": [x for x in self.form_fields if "society" in x][0],
            "round_show_treatment": round_show_treatment,
            "round_ML_outputs": round_ML_outputs
        })
        
        return round_dict


class WaitRoom(Page, SurveyPage):
    form_model = 'player'

    def before_next_page(self):
        participant = self.participant
        player = self.player
        player.case_label = str(participant.vars["case_rounds"][player.round_number])
        player.treatment_bool = participant.vars["treatment"][player.case_label]

    def vars_for_template(self):
        return dict(
            include_title = True
        )

page_sequence = [Assessment, WaitRoom]
