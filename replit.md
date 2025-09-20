# VeroctaAI - AI-Powered Financial Intelligence Platform

## Project Overview
This is a professional-grade full-stack financial analysis platform that combines React TypeScript frontend with Python Flask backend. The application provides AI-powered insights, comprehensive SpendScore analytics, and modern web interface for financial intelligence.

## Current State
- **Status**: ✅ Successfully imported and fully configured for Replit environment
- **Frontend**: React 18 with TypeScript, Tailwind CSS, and Vite build system (✅ Built)
- **Backend**: Flask with CORS, JWT authentication, OpenAI integration (✅ Running)
- **Port Configuration**: Running on port 5000 (Flask serves both API and built frontend)
- **Dependencies**: ✅ All frontend and backend dependencies installed
- **Deployment**: ✅ Configured for production with autoscale and Gunicorn

## Architecture
- **Frontend**: React TypeScript app located in `verocta-ai-unified/frontend/`
- **Backend**: Python Flask API in `verocta-ai-unified/backend/`
- **Build System**: Vite for frontend builds, Flask serves static files from `frontend/dist/`
- **Database**: Configured for Supabase PostgreSQL (optional, defaults to in-memory)

## Key Features
- SpendScore Engine with 6-metric weighted financial health calculation
- AI integration with OpenAI GPT-4o for financial recommendations
- Professional PDF report generation with charts
- Modern React components with responsive design
- JWT authentication system
- CSV processing for QuickBooks, Wave, Revolut, Xero formats

## Environment Configuration
- Flask configured to run on `0.0.0.0:5000` for Replit compatibility
- Environment variables set in `verocta-ai-unified/.env`
- Frontend build configured with proper host allowances for Replit proxy

## Recent Changes (Import Setup - September 20, 2025)
- ✅ Installed Node.js 20 and Python 3.11 language modules
- ✅ Installed all project dependencies (npm + pip)
- ✅ Created environment configuration (.env) with Replit-compatible settings
- ✅ Built React frontend for production (Vite build successful)
- ✅ Fixed Flask host binding to `0.0.0.0:5000` for Replit compatibility
- ✅ Configured workflow "VeroctaAI Server" running Flask backend
- ✅ Verified frontend serving correctly (React app + static assets)
- ✅ Verified API endpoints working (health check + logo serving)
- ✅ Configured production deployment with autoscale and Gunicorn
- ✅ Application fully functional with in-memory storage

## User Preferences
- Project follows existing coding conventions and structure
- Maintains compatibility with multiple deployment platforms (Render, Vercel, Replit)
- Uses TypeScript for frontend type safety
- Follows Flask best practices for backend API design

## Next Steps for Users
1. **Optional**: Set `OPENAI_API_KEY` in environment for AI features
2. **Optional**: Configure Supabase database credentials for persistence
3. **Ready**: Application is fully functional with in-memory storage for testing
4. **Deploy**: Use Replit's deploy feature for production deployment