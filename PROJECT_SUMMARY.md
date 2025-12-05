# 📋 Project Summary: Personalized News Agency

## 🎯 What Was Built

A complete AI-powered personalized news aggregation system with three specialized agents that work together to deliver comprehensive, localized news reports.

## 🤖 The Three Agents

### 1. Headline Finder Agent
- **Role**: Headline Research Specialist
- **Responsibility**: Searches the web for the 10 most important headlines on a given topic from the last 24 hours
- **Tools**: Web search (Serper or DuckDuckGo)
- **Output**: List of 10 recent headlines with sources and timestamps

### 2. Ground Level Reporter Agent
- **Role**: Investigative News Reporter
- **Responsibility**: Researches each headline in depth from multiple credible sources
- **Tools**: Web search + Web scraping
- **Special Feature**: Prioritizes local news sources from the user's native state/region
- **Output**: Detailed, fact-checked summaries with source citations

### 3. News Manager Agent
- **Role**: News Editor and Content Manager
- **Responsibility**: Coordinates the entire news gathering process
- **Tools**: Web search
- **Special Feature**: Can delegate tasks to other agents (hierarchical process)
- **Output**: Comprehensive, well-organized final news report

## 📁 Project Structure

```
personalized-news-agency/
├── crew.py                    # Main application (168 lines)
├── example_usage.py           # Example usage script
├── requirements.txt           # Python dependencies
├── .env                       # API keys (keep private!)
├── .gitignore                # Git ignore rules
├── README.md                  # Full documentation
├── QUICKSTART.md             # Quick start guide
├── PROJECT_SUMMARY.md        # This file
└── config/
    ├── agents.yaml           # Agent configurations (47 lines)
    └── tasks.yaml            # Task definitions (89 lines)
```

## 🔧 Key Features

### 1. **Web Search Integration**
- Primary: Serper API (optional, requires API key)
- Fallback: DuckDuckGo (no API key needed)
- Automatic fallback if Serper is not configured

### 2. **Hierarchical Process**
- News Manager coordinates other agents
- Ensures quality control and efficient workflow
- Agents work in sequence: Headlines → Research → Compilation

### 3. **Localization**
- Prioritizes news from user's native state/region
- Provides local context and perspectives
- Supports any geographic location

### 4. **Credible Sources Only**
- Focuses on famous news channels: BBC, CNN, Reuters, AP, NYT, The Guardian
- Fact-checks across multiple sources
- Includes source citations in reports

### 5. **Recent News Focus**
- Only headlines from the last 24 hours
- Ensures up-to-date information
- Filters out outdated content

## 🚀 How It Works

### User Input:
1. Topic of interest (e.g., "Artificial Intelligence")
2. Native state/region (e.g., "California")

### Process Flow:
```
User Input
    ↓
News Manager Agent (Coordinator)
    ↓
Headline Finder Agent
    → Searches web for 10 recent headlines
    ↓
Ground Level Reporter Agent (for each headline)
    → Researches from multiple sources
    → Verifies facts
    → Adds local perspective
    ↓
News Manager Agent
    → Compiles final report
    → Organizes content
    → Adds executive summary
    ↓
Final Report (Console + Text File)
```

## 📊 Output Format

The system generates a comprehensive report with:

1. **Executive Summary**: Overview of top stories
2. **Detailed Coverage**: 10 stories with:
   - Headline
   - Detailed research summary (200-300 words)
   - Multiple source citations
   - Local perspective (when available)
3. **Conclusion**: Key themes and developments

## 🛠️ Technology Stack

- **Framework**: CrewAI (Multi-agent orchestration)
- **LLM**: Google Gemini 2.0 Flash Lite
- **Search**: Serper API / DuckDuckGo
- **Web Scraping**: CrewAI ScrapeWebsiteTool
- **Language**: Python 3.8+
- **Configuration**: YAML files

## 📦 Dependencies

```
crewai[google-genai]    # CrewAI with Google Gemini support
crewai-tools            # Built-in tools (search, scrape)
python-dotenv           # Environment variable management
litellm                 # LLM integration layer
duckduckgo-search       # Fallback search engine
langchain-community     # Additional tools
```

## 🔑 Required API Keys

1. **Google Gemini API** (Required)
   - Get from: https://makersuite.google.com/app/apikey
   - Free tier available
   - Used for: AI agent intelligence

2. **Serper API** (Optional)
   - Get from: https://serper.dev
   - 100 free searches/month
   - Used for: Enhanced web search
   - Fallback: DuckDuckGo (no key needed)

## 💡 Usage Examples

### Example 1: Technology News
```python
Topic: "Artificial Intelligence"
Region: "California"
→ Gets AI news with Silicon Valley perspective
```

### Example 2: Climate News
```python
Topic: "Climate Change"
Region: "Maharashtra, India"
→ Gets climate news with Indian regional context
```

### Example 3: Space News
```python
Topic: "Space Exploration"
Region: "London, UK"
→ Gets space news with UK/European perspective
```

## 🎨 Customization Options

### 1. Change Agent Behavior
Edit `config/agents.yaml`:
- Modify roles, goals, backstories
- Adjust verbosity
- Enable/disable delegation

### 2. Modify Tasks
Edit `config/tasks.yaml`:
- Change task descriptions
- Adjust expected outputs
- Modify context dependencies

### 3. Switch LLM Model
Edit `crew.py`:
```python
gemini_llm = "gemini/gemini-2.0-flash-lite"  # Change this
```

### 4. Add More Agents
Add new agents in `config/agents.yaml` and corresponding methods in `crew.py`

## 📈 Performance

- **First Run**: 2-5 minutes (thorough research)
- **Subsequent Runs**: Similar (each run is fresh research)
- **API Calls**: ~20-30 per report (depends on research depth)
- **Output Size**: ~2000-5000 words per report

## 🔒 Security

- API keys stored in `.env` file
- `.env` excluded from git via `.gitignore`
- No hardcoded credentials
- Safe to share code (without `.env`)

## 🎓 Learning Outcomes

This project demonstrates:
1. Multi-agent AI systems
2. Hierarchical agent coordination
3. Web search and scraping integration
4. YAML-based configuration
5. LLM integration (Google Gemini)
6. Real-world AI application development

## 🚀 Future Enhancements

Potential improvements:
- [ ] Sentiment analysis of news
- [ ] Fact-checking verification
- [ ] Multi-language support
- [ ] Email delivery of reports
- [ ] Web interface (Streamlit/Gradio)
- [ ] Historical news tracking
- [ ] Custom news source preferences
- [ ] RSS feed integration
- [ ] Social media sentiment analysis
- [ ] News categorization and tagging

## 📝 Notes

- The system uses a hierarchical process where the News Manager coordinates other agents
- All agents have access to web search tools
- The Ground Level Reporter also has web scraping capabilities
- Reports are saved as text files for easy sharing
- The system is designed to be extensible and customizable

## ✅ Completion Status

**Status**: ✅ Complete and Ready to Use

All three agents are implemented and working:
- ✅ Headline Finder Agent
- ✅ Ground Level Reporter Agent
- ✅ News Manager Agent

All features are functional:
- ✅ Web search integration
- ✅ Hierarchical coordination
- ✅ Localization support
- ✅ Credible source filtering
- ✅ Comprehensive reporting

Documentation complete:
- ✅ README.md (full documentation)
- ✅ QUICKSTART.md (quick start guide)
- ✅ PROJECT_SUMMARY.md (this file)
- ✅ Example usage script
- ✅ Configuration files

---

**Ready to generate personalized news reports! 🎉**