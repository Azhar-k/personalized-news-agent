# 🗞️ Personalized News Agency - AI-Powered News Aggregator

A sophisticated AI-powered news aggregation system built with CrewAI and Google Gemini that delivers personalized news reports based on your interests and location.

## 🌟 Features

### Three Specialized AI Agents:

1. **Headline Finder Agent** 🔍
   - Searches the web for the 10 most important headlines on your chosen topic
   - Focuses on news from the last 24 hours
   - Prioritizes credible news sources

2. **Ground Level Reporter Agent** 📰
   - Conducts in-depth research on each headline
   - Verifies information across multiple credible sources (BBC, CNN, Reuters, AP, etc.)
   - Provides local perspective from your native state/region when available
   - Creates concise, accurate summaries

3. **News Manager Agent** 👔
   - Coordinates the entire news gathering process
   - Compiles comprehensive, well-organized final reports
   - Ensures local relevance and context

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key (get it from [Google AI Studio](https://makersuite.google.com/app/apikey))
- (Optional) Serper API key for enhanced web search (get it from [serper.dev](https://serper.dev))

### Installation

1. **Clone or download this repository**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API keys:**
   
   Edit the `.env` file and add your API keys:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   # Optional: For better search results
   SERPER_API_KEY=your_serper_api_key_here
   ```

   **Note:** If you don't have a Serper API key, the app will automatically use DuckDuckGo search (no API key required).

## 📖 Usage

### Run the application:

```bash
python crew.py
```

### You'll be prompted to enter:

1. **Topic of Interest**: The subject you want news about (e.g., "Artificial Intelligence", "Climate Change", "Space Exploration")
2. **Native State/Region**: Your location for localized news perspective (e.g., "California", "Maharashtra", "London")

### Example:

```
Enter the topic you're interested in: Artificial Intelligence
Enter your native state/region: California

📰 Generating personalized news report...
   Topic: Artificial Intelligence
   Region: California
```

The system will:
1. Find the 10 most recent and important headlines about your topic
2. Research each headline in detail from multiple credible sources
3. Compile a comprehensive news report with local context
4. Save the report to a text file

## 📁 Project Structure

```
.
├── crew.py                 # Main application file
├── requirements.txt        # Python dependencies
├── .env                   # API keys (keep this private!)
├── README.md              # This file
└── config/
    ├── agents.yaml        # Agent configurations
    └── tasks.yaml         # Task definitions
```

## 🔧 Configuration

### Agents (config/agents.yaml)
Defines the three AI agents with their roles, goals, and backstories.

### Tasks (config/tasks.yaml)
Defines the tasks each agent performs:
- `find_headlines_task`: Find recent headlines
- `research_headline_task`: Research headline details
- `compile_news_report_task`: Create final report

### Customization

You can customize the agents and tasks by editing the YAML files:

- **Change agent behavior**: Edit `config/agents.yaml`
- **Modify task requirements**: Edit `config/tasks.yaml`
- **Switch LLM model**: Change `gemini_llm` in `crew.py`

## 🛠️ Advanced Features

### Using Serper API for Better Search

For more accurate and comprehensive search results, sign up for a free Serper API key:

1. Go to [serper.dev](https://serper.dev)
2. Sign up for a free account (100 free searches/month)
3. Copy your API key
4. Add it to your `.env` file:
   ```
   SERPER_API_KEY=your_key_here
   ```

### Hierarchical Process

The crew uses a hierarchical process where the News Manager agent coordinates the other agents, ensuring efficient workflow and quality control.

## 📊 Output

The application generates:

1. **Console Output**: Real-time progress and verbose logging
2. **Text File**: A saved report named `news_report_[topic].txt`

### Report Structure:

```
# Personalized News Report: [Your Topic]
## For: [Your Region]
## Date: [Current Date]

### Executive Summary
[Overview of top stories]

### Detailed Coverage

#### Story 1: [Headline]
[Detailed research and summary]
Sources: [List of sources]

[... continues for all 10 headlines ...]

### Conclusion
[Key themes and developments]
```

## 🔍 Troubleshooting

### Common Issues:

1. **"GEMINI_API_KEY not set"**
   - Make sure you've added your API key to the `.env` file
   - Ensure the `.env` file is in the same directory as `crew.py`

2. **Import errors**
   - Run: `pip install -r requirements.txt`
   - Make sure you're using Python 3.8+

3. **Search not working**
   - The app will automatically fall back to DuckDuckGo if Serper is not configured
   - For better results, add a Serper API key

4. **Slow performance**
   - First run may be slower as agents learn
   - Consider using Serper API for faster search results
   - Check your internet connection

## 🤝 Contributing

Feel free to enhance this project by:
- Adding more news sources
- Improving agent prompts
- Adding new features (sentiment analysis, fact-checking, etc.)
- Supporting more languages

## 📝 License

This project is open source and available for educational and personal use.

## 🙏 Acknowledgments

- Built with [CrewAI](https://www.crewai.com/)
- Powered by [Google Gemini](https://deepmind.google/technologies/gemini/)
- Search capabilities via [Serper](https://serper.dev) or [DuckDuckGo](https://duckduckgo.com)

## 📧 Support

For issues or questions, please check the troubleshooting section or review the CrewAI documentation.

---

**Happy News Reading! 📰✨**