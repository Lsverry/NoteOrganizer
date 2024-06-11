from django import template

# Register a custom template tag library
register = template.Library()

@register.filter(name='add_class')
def add_class(field, css):
    """
    Adds a CSS class to a form field widget.
    
    This custom filter allows you to add a CSS class to the widget of a form field.
    It's useful for styling form fields using Bootstrap or other CSS frameworks.
    """
    # Apply the specified CSS class to the form field widget
    return field.as_widget(attrs={"class": css})