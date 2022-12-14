from email.policy import default
import pickle, random
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
    name_in_url = 'assessment'
    players_per_group = None
    _CASES = [
        "A", "B", "C", "D", "E", "F", "G", "H", 
        "I", "J", "K", "L", "M", "N", "O", "P"
    ]
    _NUM_ROUNDS = len(_CASES)
    num_rounds = _NUM_ROUNDS

    with open("_rooms/innovasjon_norge_experiment.txt") as infile:
        _LABELS = [line.rstrip("\n") for line in infile]

class Subsession(BaseSubsession):
    import random
    random.seed(42)
    def creating_session(subsession):
        for p, label in zip(subsession.get_players(), Constants._LABELS):
            p.participant.label = label
            
        if subsession.round_number == 1:
            with open("inputs/treatments.pkl", "rb") as infile:
                treatments = pickle.load(infile)
            
            for i, p in enumerate(subsession.get_players()):
                round_numbers = list(range(1, Constants._NUM_ROUNDS+1))
                random.shuffle(round_numbers)
                p.participant.vars['case_rounds'] = dict(zip(round_numbers, Constants._CASES))
                p.participant.vars['treatment'] = treatments[i+1]

class Group(BaseGroup):
    pass


class Player(BasePlayer):

    app_con_size = models.StringField(
        choices=[
            ('small', _('Liten')),
            ('medium', _('Mellomstor')),
            ('large', _('Stor'))
        ],
        widget=widgets.RadioSelect
    )

    app_con_owner_comment = models.LongStringField(
        label="",
        blank=True
    )

    app_con_habilitation_conflict = models.LongStringField(
        label="",
        blank=True
    )

    app_con_score_innovative = models.StringField(
        choices=[
            ('good', _('God')),
            ('average', _('Middels')),
            ('poor', _('Svak'))
        ],
        blank=False,
        widget=widgets.RadioSelect
    )

    app_con_comment_innovative = models.LongStringField(
        label="",
        blank=True
    )

    app_con_score_prospects = models.StringField(
        choices=[
            ('good', _('God')),
            ('average', _('Middels')),
            ('poor', _('Svak'))
        ],
        blank=False,
        widget=widgets.RadioSelect
    )

    app_con_comment_prospects = models.LongStringField(
        label="",
        blank=True
    )

    app_con_score_feasibility = models.StringField(
        choices=[
            ('good', _('God')),
            ('average', _('Middels')),
            ('poor', _('Svak'))
        ],
        blank=False,
        widget=widgets.RadioSelect
    )

    app_con_comment_feasibility = models.LongStringField(
        label="",
        blank=True
    )

    app_con_sustainability = models.LongStringField(
        label="",
        blank=True
    )

    app_con_other_comments = models.LongStringField(
        label="",
        blank=True
    )

    app_con_women = models.StringField(
        choices=[
            ('no_choice', _('Ikke valgt')),
            ('yes', _('Ja')),
            ('no', _('Nei'))
        ],
        blank=True,
        widget=widgets.RadioSelect
    )
    
    app_con_w_1 = models.BooleanField(
        label=_('Medeier eller oppstart'),
        widget=widgets.CheckboxInput,
        blank=True,
    )
    
    app_con_w_2 = models.BooleanField(
        label=_('Kompetanse??kning'),
        widget=widgets.CheckboxInput,
        blank=True,
    )
    
    app_con_w_3 = models.BooleanField(
        label=_('> 30 \% av styre eller ledelse'),
        widget=widgets.CheckboxInput,
        blank=True,
    )
    
    app_con_w_4 = models.BooleanField(
        label=_('??ke kvinners deltakelse'),
        widget=widgets.CheckboxInput,
        blank=True,
    )

    app_con_risk = models.IntegerField(
        choices=[
            (1, "1 - Lav"),
            (2, "2"),
            (3, "3"),
            (4, "4"),
            (5, "5"),
            (6, "6 - H??y")
        ],
        blank=True
    )

    app_con_businessrisk = models.StringField(
        choices=[
            ("A", "A - Lav"),
            ("B", "B - Middels"),
            ("C", "C - H??y"),
            ("D", "D - Ekstra h??y")
        ],
        blank=True
    )

    app_con_innovation = models.StringField(
        choices=[
            ("business", "Innovasjon p?? bedriftsniv??"),
            ("regional", "Innovasjon p?? regionalt niv??"),
            ("national", "Innovasjon p?? nasjonalt niv??"),
            ("international", "Innovasjon p?? internasjonalt niv??"),
            ("not_applies", "Ikke relevant")
        ],
        blank=True
    )

    app_con_innovation_type = models.StringField(
        choices=[
            ("product", "Produkt-/tjenesteinnovasjon"),
            ("process", "Prosessinnovasjon"),
            ("organisation", "Organisatorisk innovasjon"),
            ("market", "Markedsmessig innovasjon")
        ],
        blank=True
    )

    app_con_sector = models.StringField(
        choices=[
            ("energy", "Energi og milj??"),
            ("health", "Helse"),
            ("agricultural", "Landbruk"),
            ("marine", "Marin"),
            ("maritime", "Maritim"),
            ("oil", "Olje og gass"),
            ("tourism", "Reiseliv"),
            ("not_listed", "Ikke satsingsomr??de")
        ],
        blank=True
    )

    app_con_environment = models.StringField(
        choices=[
            ('no_choice', _('Ikke valgt')),
            ('yes', _('Ja')),
            ('no', _('Nei'))
        ],
        blank=True,
        widget=widgets.RadioSelect
    )

    app_con_e_1 = models.BooleanField(
        label=_('Produksjon av fornybar energi'),
        widget=widgets.CheckboxInput,
        blank=True,
    )
    
    app_con_e_2 = models.BooleanField(
        label=_('Reduksjon i utslipp av klimagasser'),
        widget=widgets.CheckboxInput,
        blank=True,
    )
    
    app_con_e_3 = models.BooleanField(
        label=_('Vannbehandling'),
        widget=widgets.CheckboxInput,
        blank=True,
    )
    
    app_con_e_4 = models.BooleanField(
        label=_('Bedre utnyttelse av biologiske ressurser'),
        widget=widgets.CheckboxInput,
        blank=True,
    )
    
    app_con_e_5 = models.BooleanField(
        label=_('Energieffektivisering'),
        widget=widgets.CheckboxInput,
        blank=True,
    )
    
    app_con_e_6 = models.BooleanField(
        label=_('Andre tiltak/l??sninger'),
        widget=widgets.CheckboxInput,
        blank=True,
    )
    
    app_con_e_7 = models.BooleanField(
        label=_('Redusert luftforurensing ellers'),
        widget=widgets.CheckboxInput,
        blank=True,
    )
    
    app_con_e_8 = models.BooleanField(
        label=_('Energiutnyttelse av avl??psr??r, avl??psslam, spillvarme, avgasser (Waste to energy)'),
        widget=widgets.CheckboxInput,
        blank=True,
    )
    
    app_con_e_9 = models.BooleanField(
        label=_('Bedre utnyttelse av uorganiske ressurser og mineraler'),
        widget=widgets.CheckboxInput,
        blank=True,
    )
    
    app_con_e_10 = models.BooleanField(
        label=_('Materialgjenvinning'),
        widget=widgets.CheckboxInput,
        blank=True,
    )
    
    app_con_e_11 = models.BooleanField(
        label=_('Redusert bruk av kjemikalier, antibiotika, andre skadelige stoffer'),
        widget=widgets.CheckboxInput,
        blank=True,
    )
    
    app_con_society = models.StringField(
        choices=[
            ('no_choice', _('Ikke valgt')),
            ('yes', _('Ja')),
            ('no', _('Nei'))
        ],
        blank=True,
        widget=widgets.RadioSelect
    )

    app_con_s_1 = models.BooleanField(
        label=_('Helse og velferd'),
        widget=widgets.CheckboxInput,
        blank=True,
    )
    
    app_con_s_2 = models.BooleanField(
        label=_('Et tryggere samfunn / ??kt beredskap og sikkerhet'),
        widget=widgets.CheckboxInput,
        blank=True,
    )
    
    app_con_s_3 = models.BooleanField(
        label=_('??kt dyrevelferd'),
        widget=widgets.CheckboxInput,
        blank=True,
    )
    
    app_con_s_4 = models.BooleanField(
        label=_('??kt tilgang p?? utdanning, forskning eller andre kunnskapshevende tiltak'),
        widget=widgets.CheckboxInput,
        blank=True,
    )
    
    app_con_s_5 = models.BooleanField(
        label=_('L??sninger p?? andre utfordringer i samfunnet, nasjonalt eller internasjonalt'),
        widget=widgets.CheckboxInput,
        blank=True,
    )

    app_con_coststudy_offered = models.IntegerField(
        blank=True,
    )

    app_con_costmws_offered = models.IntegerField(
        blank=True,
    )

    app_con_costnetwork_offered = models.IntegerField(
        blank=True,
    )
    
    app_con_costcomp_offered = models.IntegerField(
        blank=True,
    )   

    app_con_INfund_finoffered = models.IntegerField(
        blank=True,
    )
        
    app_con_AFfund_finoffered = models.IntegerField(
        blank=True,
    )

    app_con_partial_funding = models.LongStringField(
        label="",
        blank=True
    )

    app_con_no_funding = models.LongStringField(
        label="",
        blank=True
    )

    app_con_internal_comment = models.LongStringField(
        label="",
        blank=True
    )

    case_label = models.LongStringField(blank=False)

    treatment_bool = models.IntegerField(blank=False)