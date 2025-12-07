# 🚀 Quick Start Guide

Get your personalized news app running in 5 minutes!

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 2: Set Up API Key

1. Get your free Google Gemini API key from: https://makersuite.google.com/app/apikey

2. Open the `.env` file and add your key:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```

## Step 3: Run the App

```bash
python crew.py
```

## Step 4: Enter Your Preferences

When prompted, enter:
- **Topic**: What you want news about (e.g., "Technology", "Sports", "Politics")
- **Region**: Your location (e.g., "California", "New York", "London")

## Example Session

```
Enter the topic you're interested in: Artificial Intelligence
Enter your native state/region: California

📰 Generating personalized news report...
   Topic: Artificial Intelligence
   Region: California
```

The app will:
1. ✅ Find 2 recent headlines about AI
2. ✅ Research each headline from multiple sources
3. ✅ Create a comprehensive report with local context
4. ✅ Save the report to a file

## Output

You'll get:
- Real-time progress in the console
- A saved text file: `news_report_artificial_intelligence.txt`

## Tips

- **First run may take 2-5 minutes** as the AI agents research thoroughly
- **Be specific with topics** for better results (e.g., "AI in Healthcare" vs just "AI")
- **Include country/state** in region for better local news (e.g., "Maharashtra, India")

## Optional: Better Search Results

For more accurate search, get a free Serper API key:

1. Sign up at: https://serper.dev (20 free searches/month)
2. Add to `.env`:
   ```
   SERPER_API_KEY=your_serper_key_here
   ```

## Troubleshooting

**Problem**: "GEMINI_API_KEY not set"
- **Solution**: Make sure you added your API key to the `.env` file

**Problem**: Import errors
- **Solution**: Run `pip install -r requirements.txt` again

**Problem**: Slow performance
- **Solution**: This is normal for the first run. The AI needs time to research thoroughly.

## What's Next?

- Try different topics and regions
- Check the full README.md for advanced features
- Customize agents in `config/agents.yaml`

---

**Need Help?** Check the full README.md or the troubleshooting section.