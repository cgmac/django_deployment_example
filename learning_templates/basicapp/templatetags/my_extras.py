from django import template

register = template.Library()

# Write the Custom Template Filter

# register using decorators
@register.filter(name='cup')

# function
def cup(value,arg):
    """
    This cuts out all values of "arg" from the string
    """
    return value.replace(arg,'')

# we can do this with decorators
# register.filter('cup',cup)
