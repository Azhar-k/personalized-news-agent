import os
from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from dotenv import load_dotenv

# Load environment variables
load_dotenv() 
if not os.getenv("GEMINI_API_KEY"):
    print("Error: GEMINI_API_KEY environment variable not set.")
    exit()

# --- 1. Configure the Gemini LLM ---
gemini_llm = "gemini/gemini-2.5-flash-lite"

# --- 2. Initialize Search Tools ---
# Note: SerperDevTool requires SERPER_API_KEY in .env
# Alternative: Use DuckDuckGo search which doesn't require API key
try:
    from crewai_tools import SerperDevTool
    search_tool = SerperDevTool()
    print("Using SerperDevTool for web search")
except:
    # Fallback to DuckDuckGo if Serper is not configured
    from langchain_community.tools import DuckDuckGoSearchRun
    search_tool = DuckDuckGoSearchRun()
    print("Using DuckDuckGo for web search (no API key required)")

scrape_tool = ScrapeWebsiteTool()

# --- 3. Define the News Crew Base Class ---
@CrewBase
class NewsAgencyCrew:
    """Personalized News Agency Crew"""
    
    # Specify the paths to your configuration files
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # --- Agent Definitions ---
    
    @agent
    def headline_finder(self) -> Agent:
        """Agent that finds the latest headlines on a given topic"""
        return Agent(
            **self.agents_config['headline_finder'],
            llm=gemini_llm,
            tools=[search_tool]
        )
    
    @agent
    def ground_level_reporter(self) -> Agent:
        """Agent that researches detailed information about headlines"""
        return Agent(
            **self.agents_config['ground_level_reporter'],
            llm=gemini_llm,
            tools=[search_tool, scrape_tool]
        )
    
    @agent
    def news_manager(self) -> Agent:
        """Manager agent that coordinates the news gathering process"""
        return Agent(
            **self.agents_config['news_manager'],
            llm=gemini_llm,
            tools=[search_tool]
        )

    # --- Task Definitions ---
    
    @task
    def find_headlines_task(self) -> Task:
        """Task to find the latest headlines"""
        config = self.tasks_config['find_headlines_task'].copy()
        config.pop('agent', None)
        return Task(
            **config,
            agent=self.headline_finder()
        )
    
    @task
    def research_headline_task(self) -> Task:
        """Task to research detailed information about a headline"""
        config = self.tasks_config['research_headline_task'].copy()
        config.pop('agent', None)
        return Task(
            **config,
            agent=self.ground_level_reporter()
        )
    
    @task
    def compile_news_report_task(self) -> Task:
        """Task to compile the final news report"""
        config = self.tasks_config['compile_news_report_task'].copy()
        config.pop('agent', None)
        return Task(
            **config,
            agent=self.news_manager()
        )

    # --- Crew Assembly ---
    
    @crew
    def news_crew(self) -> Crew:
        """Assembles the news agency crew"""
        return Crew(
            agents=[
                self.headline_finder(),
                self.ground_level_reporter(),
                self.news_manager()
            ],
            tasks=[
                self.find_headlines_task(),
                self.research_headline_task(),
                self.compile_news_report_task()
            ],
            process=Process.hierarchical,
            manager_llm=gemini_llm,
            verbose=True,
        )

# --- 4. Main execution ---
if __name__ == "__main__":
    print("=" * 70)
    print("🗞️  PERSONALIZED NEWS AGENCY - Powered by CrewAI & Gemini")
    print("=" * 70)
    
    # Get user inputs
    print("\n📋 Please provide the following information:\n")
    
    topic = input("Enter the topic you're interested in (e.g., 'Artificial Intelligence', 'Climate Change'): ").strip()
    if not topic:
        topic = "Technology"
        print(f"No topic provided. Using default: {topic}")
    
    native_state = input("Enter your native state/region (e.g., 'California', 'Maharashtra', 'London'): ").strip()
    if not native_state:
        native_state = "United States"
        print(f"No state provided. Using default: {native_state}")
    
    print("\n" + "=" * 70)
    print(f"📰 Generating personalized news report...")
    print(f"   Topic: {topic}")
    print(f"   Region: {native_state}")
    print("=" * 70 + "\n")
    
    # Prepare inputs for the crew
    inputs = {
        'topic': topic,
        'native_state': native_state,
        'headline': ''  # This will be populated by the workflow
    }
    
    # Kickoff the crew execution
    try:
        result = NewsAgencyCrew().news_crew().kickoff(inputs=inputs)
        
        print("\n\n" + "=" * 70)
        print("📊 FINAL NEWS REPORT")
        print("=" * 70)
        print(result)
        
        # Optionally save the report to a file
        output_filename = f"news_report_{topic.replace(' ', '_').lower()}.txt"
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(str(result))
        print(f"\n✅ Report saved to: {output_filename}")
        
    except Exception as e:
        print(f"\n❌ Error generating news report: {str(e)}")
        print(e)

# Made with Bob
