from os import environ
import otree_startup

SESSION_CONFIGS = [
    dict(
       name='innovasjon_norge_experiment',
       display_name="Innovasjon Norge experiment",
       num_demo_participants=2,
       app_sequence=['introduction', 'assessment']
    ),
]

ROOMS = [
    dict(
       name='innovasjon_norge_experiment',
       display_name="Innovasjon Norge experiment",
       participant_label_file='_rooms/innovasjon_norge_experiment.txt',
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'NOK'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'ffe=f5o-*x-8mvg72qnzlf!))(f%=r)kgx9w910!1lpvx5@nvt'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree', 'survey_extras']
