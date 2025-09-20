# 🚀 VEROCTA Financial Intelligence Platform - Unified

**Professional-grade financial analysis platform with AI-powered insights, comprehensive SpendScore analytics, and modern React frontend.**

![VEROCTA](backend/static/assets/images/verocta-logo.png)

## ✨ Features

### 🧮 SpendScore Engine
- 6-metric weighted financial health calculation
- Real-time analysis and scoring
- Comprehensive financial insights

### 🤖 AI Integration
- OpenAI GPT-4o powered recommendations
- Intelligent financial analysis
- Personalized insights and suggestions

### 🎨 Modern Frontend
- React 18 with TypeScript
- Responsive design with Tailwind CSS
- Component-based architecture
- Mobile-first approach

### 📊 Enhanced Visualizations
- Professional pie charts and analytics
- Interactive dashboards
- Real-time data visualization

### 🏢 Company Branding
- Logo upload and custom PDF reports
- Professional report generation
- Enhanced visual identity

### 🔌 REST API
- Complete API suite for integration
- RESTful endpoints
- JSON responses

## 🏗️ Architecture

```
findash-unified/
├── backend/                 # Python Flask API
│   ├── app.py              # Main Flask application
│   ├── routes.py           # API routes and handlers
│   ├── spend_score_engine.py # Core financial analysis
│   ├── csv_parser.py       # CSV processing logic
│   ├── gpt_utils.py        # AI integration
│   ├── pdf_generator.py    # Report generation
│   ├── static/             # Static assets
│   ├── templates/          # HTML templates (legacy)
│   ├── uploads/            # File uploads
│   └── outputs/            # Generated reports
├── frontend/               # React TypeScript App
│   ├── src/                # Source code
│   │   ├── components/     # React components
│   │   ├── pages/          # Page components
│   │   ├── styles/         # CSS files
│   │   └── utils/          # Utility functions
│   ├── dist/               # Built files (generated)
│   └── package.json        # Frontend dependencies
├── shared/                 # Shared resources
├── docs/                   # Documentation
├── package.json            # Unified scripts
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container configuration
└── docker-compose.yml      # Multi-service setup
```

## 🚀 Quick Start

### Prerequisites
- **Node.js** 16.0.0 or higher
- **Python** 3.11 or higher
- **OpenAI API key**

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd findash-unified
   ```

2. **Install all dependencies**
   ```bash
   npm run install:all
   ```

3. **Configure environment**
   ```bash
   cp env.template .env
   # Edit .env and add your OPENAI_API_KEY
   ```

4. **Build frontend**
   ```bash
   npm run build
   ```

5. **Start the application**
   ```bash
   npm start
   ```

6. **Access the platform**
   ```
   http://127.0.0.1:5001
   ```

## 🛠️ Development

### Development Mode
```bash
# Start both frontend and backend in development mode
npm run dev

# Or start them separately:
npm run dev:frontend  # Frontend on http://localhost:3000
npm run dev:backend   # Backend on http://127.0.0.1:5001
```

### Available Scripts

| Script | Description |
|--------|-------------|
| `npm run dev` | Start both frontend and backend in development |
| `npm run build` | Build frontend for production |
| `npm start` | Start production server |
| `npm run install:all` | Install all dependencies |
| `npm run lint` | Run ESLint on frontend |
| `npm run test` | Run frontend tests |
| `npm run clean` | Clean build artifacts |

## 📊 SpendScore Metrics

| Metric | Weight | Description |
|--------|--------|-------------|
| Frequency Score | 15% | Transaction frequency patterns |
| Category Diversity | 10% | Spending category distribution |
| Budget Adherence | 20% | Spending vs. expected patterns |
| Redundancy Detection | 15% | Duplicate/similar transactions |
| Spike Detection | 20% | Unusual large transactions |
| Waste Ratio | 20% | Non-essential spending analysis |

**Score Ranges:**
- 🟩 **Green (90-100)**: Excellent financial discipline
- 🟨 **Amber (70-89)**: Good management, optimization opportunities  
- 🟥 **Red (0-69)**: Significant improvement needed

## 🔌 API Documentation

### Key Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/upload` | POST | Upload CSV and trigger analysis |
| `/api/spend-score` | GET | Get latest SpendScore metrics |
| `/api/report` | GET | Download PDF report |
| `/api/health` | GET | Health check endpoint |
| `/api/docs` | GET | API documentation |

### Example API Usage

```bash
# Upload and analyze
curl -X POST http://127.0.0.1:5001/api/upload \
  -F "file=@transactions.csv" \
  -F "companyName=My Company" \
  -F "companyLogo=@logo.png"

# Get SpendScore
curl -X GET http://127.0.0.1:5001/api/spend-score

# Download report
curl -X GET http://127.0.0.1:5001/api/report -o report.pdf
```

## 🚢 Deployment

### Docker Deployment

1. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

2. **Production deployment**
   ```bash
   # Set environment variables
   export OPENAI_API_KEY=your_key_here

   # Run production container
   docker-compose up -d
   ```

### Manual Deployment

1. **Build frontend**
   ```bash
   npm run build
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run with Gunicorn**
   ```bash
   gunicorn --bind 0.0.0.0:5001 --workers 4 backend.app:app
   ```

## 🧪 Testing

### Sample Data
Use provided sample files in `backend/samples/`:
- `quickbooks_sample.csv`
- `xero_sample.csv`
- `wave.csv`
- `revolut.csv`

### API Testing
```bash
# Health check
curl http://127.0.0.1:5001/api/health

# Test upload
curl -X POST http://127.0.0.1:5001/api/upload \
  -F "file=@backend/samples/quickbooks_sample.csv"
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API key for AI features | Required |
| `FLASK_ENV` | Flask environment | `development` |
| `FLASK_DEBUG` | Enable debug mode | `True` |
| `HOST` | Server host | `127.0.0.1` |
| `PORT` | Server port | `5001` |

### Frontend Configuration
The frontend automatically connects to the backend API. For development, ensure the backend is running on the configured port.

## 📁 Supported Formats

- **QuickBooks CSV**
- **Wave Accounting CSV**
- **Revolut CSV**
- **Xero CSV**
- **Generic transaction CSV**

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit pull request

### Code Style
- **Backend**: Follow PEP 8 Python style guide
- **Frontend**: Use TypeScript, ESLint, and Prettier
- Write meaningful commit messages
- Include tests for new features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: `/docs/`
- **API Reference**: `/api/docs`
- **Issues**: [GitHub Issues](https://github.com/findash/findash-unified/issues)
- **Email**: support@findash.com

## 🙏 Acknowledgments

- [React Team](https://reactjs.org/) for the amazing framework
- [Flask](https://flask.palletsprojects.com/) for the Python web framework
- [Tailwind CSS](https://tailwindcss.com/) for the utility-first CSS framework
- [OpenAI](https://openai.com/) for the AI capabilities

---

**VeroctaAI Financial Intelligence Platform v2.0.0 - Unified**  
*Professional financial analysis with AI-powered insights and modern web interface*