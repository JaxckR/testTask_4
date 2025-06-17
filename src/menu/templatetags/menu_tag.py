from django import template
from django.db import connection
from django.http import Http404

from menu.models import Category

register = template.Library()


def func(query: list, target: Category, memory: dict | None = None):
    if memory is None:
        memory = {
            'item': target,
            'child': [],
        }
    else:
        memory = {
            'item': target,
            'child': [
                memory
            ],
        }

    for item in query:
        if item.parent and item.parent.pk == target.pk:
            memory['child'].append(item)

    query.remove(target)
    memory['child'].sort(key=lambda x: x.name if isinstance(x, Category) else x.get('item').name)


    if target.parent is not None:
        memory = func(query, query[query.index(target.parent)], memory)

    return memory


@register.inclusion_tag('menu/template_tags/show_menu.html', takes_context=True)
def draw_menu(context, path):
    all_categories = list(Category.objects.select_related('parent').all())

    for item in all_categories:
        if item.url == path:
            current = item
            break
    else:
        raise Http404

    tree = func(all_categories, current)

    return {'menu_tree': [tree], 'current': current}
