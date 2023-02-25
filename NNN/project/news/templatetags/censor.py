from django import template

register = template.Library()

@register.filter()
def currency(value):
    stopfilter = ["дурак", "морда", "помогите"]

    for word in value.split():
        if word.lower() in stopfilter:
            value = value.replace(word, f"{word[0]}{'*' * (len(word) - 1)}")
    return value

