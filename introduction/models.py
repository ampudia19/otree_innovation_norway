import random

from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
from django.utils.translation import ugettext_lazy as _

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'introduction'
    players_per_group = None
    num_rounds = 1
    num_proposals = 8


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    ###########################################################################
    ############################# Consent #####################################
    ###########################################################################

    con_read = models.BooleanField(
        label=_('I have read and understood the above information.'),
        widget=widgets.CheckboxInput,
    )

    con_doubts = models.BooleanField(
        label=_('I have had the opportunity to have any questions about this project answered.'),
        widget=widgets.CheckboxInput,
    )

    con_agree = models.BooleanField(
        label=_('I agree to participate in this study.'),
        widget=widgets.CheckboxInput,
    )