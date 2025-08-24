from odoo import models, fields, api
import requests
import json
import os
import logging

_logger = logging.getLogger(__name__)

class AIAgent(models.Model):
    _name = 'ai.agent'
    _description = 'AI Agent'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', default='AI Assistant', required=True)
    active = fields.Boolean(default=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('archived', 'Archived')
    ], default='active', string='Status')
    
    @api.model
    def send_message(self, message):
        """Gửi tin nhắn đến AI agent và nhận phản hồi"""
        ai_agent_url = "http://localhost:7777/query"
        headers = {'Content-Type': 'application/json'}
        payload = {
            'query': message,
            'tts_enabled': False
        }

        try:
            _logger.info(f"Sending message to AI agent at {ai_agent_url}")
            response = requests.post(
                ai_agent_url,
                headers=headers,
                json=payload,
                timeout=60  #
            )
            response.raise_for_status() #

            try:
                return response.json().get('answer', '⚠️ No answer returned from agent.')
            except json.JSONDecodeError:
                _logger.error("Invalid JSON response from agent: %s", response.text)
                return "❌ Invalid JSON response from agent."

        except requests.exceptions.Timeout:
            _logger.warning(f"Timeout connecting to AI agent at {ai_agent_url}")
            return "⏰ Timeout: AI agent did not respond."
        except requests.exceptions.ConnectionError:
            _logger.error(f"Connection error to AI agent at {ai_agent_url}")
            return "🔌 Connection error: Could not connect to AI agent service. Please make sure it's running."
        except requests.exceptions.HTTPError as e:
            _logger.error(f"HTTP Error from agent: {e.response.status_code} - {e.response.text}")
            return f"❗HTTP Error: {e.response.status_code} - {e.response.text}"
        except Exception as e:
            _logger.error(f"An unexpected error occurred: {str(e)}")
            return f"Error: {str(e)}"