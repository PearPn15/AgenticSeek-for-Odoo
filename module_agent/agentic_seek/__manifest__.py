{
    'name': 'AI Agent Integration',
    'version': '17.0.1.0.0',
    'category': 'Tools',
    'summary': 'Integrates AI Agent with Odoo',
    'description': """
        This module integrates the AI Agent with Odoo, providing a chat interface
        for interacting with the AI assistant.
    """,
    'license': 'LGPL-3',
    'author': 'Cory Hisey',
    'website': 'https://coryhisey.com',
    'depends': ['base', 'web', 'mail'],
    'data': [
        'views/agentic_chat_views.xml',
        'views/agentic_menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'agentic_seek/static/src/css/agentic_chat.css',
            'agentic_seek/static/src/js/agentic_chat_form_view.js',
            'agentic_seek/static/src/xml/agentic_chat_templates.xml',
        ],
    },
    'images': ['static/images/changing-sales-order.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}