from survey_extras.views import SurveyPage

from ._builtin import Page
from .models import Player, Constants

doc = """
    Documentation
"""


class Start(Page, SurveyPage):
    """
    Start screen. [DAV] There should be some variable confirmation.
    """
    def vars_for_template(self):
        id = self.participant.id_in_session
        # some_var_getter = self.player.set_vars()
        return {
            "include_title": True,
            'id': id,
            'error_msgs': None, # should report error in form (ie. you are not assigned an ID); from some_var_getter
            # any other dict returns
        }

class Consent(Page, SurveyPage):
    form_model = 'player'
    form_fields = [f.name for f in Player._meta.fields if f.name.startswith('con_')]
    def vars_for_template(self):
        return {
            "include_title": True,
        }

class Instructions(Page, SurveyPage):
    # How explicit should we be with the instructions? Also, present the reason for the study (VAGUELY), and the likely additional screen they are likely to see (ML output)
    def vars_for_template(self):
        return {
            "num_proposals": Constants.num_proposals,
            "include_title": True,
        }

page_sequence = [Start, Consent, Instructions]
