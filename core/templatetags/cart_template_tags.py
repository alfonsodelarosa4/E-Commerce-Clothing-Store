from django import template
from core.models import Order

register = template.Library()

# sets up cart count on navbar>
@register.filter
def cart_item_count(user):
    # if user is signed in
    if user.is_authenticated:
        # get unordered order
        qs = Order.objects.filter(user=user, ordered=False)
        # if unordered order exists
        if qs.exists():
            # return number of unordered orders
            return qs[0].items.count()
    return 0
