def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    categories = []
    for category in mapping['categoryIdsSorted']:
        items = []

        for role in mapping['categories'][category]['roleIds']:
            items += [{'id': role,
                       'text': mapping['roles'][role]['name']}]

        categories += [{'id': 'category-' + category,
                        'text': mapping['categories'][category]['name'],
                        'items': items}]

    return {'categories': categories}
