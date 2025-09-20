"""
Vercel Serverless Function Entry Point
Lightweight serverless functions for VeroctaAI API endpoints
"""

import sys
import os
import json
from datetime import datetime

# Add the project root to the Python path for imports
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

def api_response(status_code, data=None, message=None):
    """Helper function to create consistent API responses"""
    response = {
        "status": "success" if status_code < 400 else "error",
        "timestamp": datetime.utcnow().isoformat()
    }
    
    if data is not None:
        response["data"] = data
    if message:
        response["message"] = message
    
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type, Authorization, Accept"
        },
        "body": json.dumps(response)
    }

def handler(event, context):
    """
    Main Vercel serverless function handler
    Routes requests to appropriate functions
    """
    # Get the HTTP method and path
    method = event.get('httpMethod', 'GET')
    path = event.get('path', '/')
    
    # Handle CORS preflight requests
    if method == 'OPTIONS':
        return api_response(200, message="CORS preflight")
    
    # Health check endpoint
    if path.endswith('/health') or path.endswith('/api/health'):
        return api_response(200, {
            "status": "healthy",
            "service": "VeroctaAI API",
            "version": "2.0.0",
            "deployment": "vercel-serverless"
        })
    
    # Default response for unhandled routes
    return api_response(404, message="Endpoint not found in serverless deployment")

# Export for Vercel
app = handler