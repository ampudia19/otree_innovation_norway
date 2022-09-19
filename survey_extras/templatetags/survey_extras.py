from django import template
from django.utils.translation import ugettext_lazy as _

register = template.Library()


@register.inclusion_tag('survey_extras/tags/BackButton.html', takes_context=True)
def back_button(context,  *args, **kwargs):
    if 'show_back' not in context:
        raise Exception(r'use SurveyPage as the super class for views that use the {% back %} button')
    return context


@register.inclusion_tag('survey_extras/tags/NavigationButtons.html', takes_context=True)
def navigation_buttons(context,  *args, **kwargs):
    if 'show_back' not in context:
        raise Exception(r'use SurveyPage as the super class for views that use the {% back %} button')
    context['show_next'] = context.get('show_next', True)
    context['next_text'] = context.get('next_text', 'Next')
    context['back_text'] = context.get('back_text', 'Back')
    return context


@register.inclusion_tag('survey_extras/tags/NavigationButtons.html', takes_context=True)
def submit_buttons(context,  *args, **kwargs):
    if 'show_back' not in context:
        raise Exception(r'use SurveyPage as the super class for views that use the {% back %} button')
    context['show_next'] = context.get('show_next', True)
    context['next_text'] = context.get('next_text', 'Submit Scores')
    return context



@register.inclusion_tag('survey_extras/tags/ProgressBar.html', takes_context=True)
def progress_bar(context,  *args, **kwargs):
    return context


@register.inclusion_tag('survey_extras/tags/FormfieldOnly.html')
def formfieldonly(field, *args, **kwargs):
    return {'field': field}
