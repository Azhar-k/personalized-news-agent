"""
Example usage of the Personalized News Agency

This script demonstrates how to use the news agency with predefined inputs.
"""

from crew import NewsAgencyCrew

def run_news_report(topic: str, native_state: str):
    """
    Generate a personalized news report
    
    Args:
        topic: The topic you're interested in
        native_state: Your native state/region for localized news
    """
    print("=" * 70)
    print("🗞️  PERSONALIZED NEWS AGENCY - Example Usage")
    print("=" * 70)
    print(f"\n📰 Generating news report...")
    print(f"   Topic: {topic}")
    print(f"   Region: {native_state}")
    print("=" * 70 + "\n")
    
    # Prepare inputs
    inputs = {
        'topic': topic,
        'native_state': native_state,
        'headline': ''
    }
    
    # Run the crew
    try:
        result = NewsAgencyCrew().news_crew().kickoff(inputs=inputs)
        
        print("\n\n" + "=" * 70)
        print("📊 FINAL NEWS REPORT")
        print("=" * 70)
        print(result)
        
        # Save to file
        output_filename = f"news_report_{topic.replace(' ', '_').lower()}.txt"
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(str(result))
        print(f"\n✅ Report saved to: {output_filename}")
        
        return result
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return None


if __name__ == "__main__":
    # Example 1: Technology news for California
    print("\n🔹 Example 1: Technology News\n")
    run_news_report(
        topic="Artificial Intelligence",
        native_state="California"
    )
    
    # Uncomment to run more examples:
    
    # # Example 2: Climate news for India
    # print("\n\n🔹 Example 2: Climate News\n")
    # run_news_report(
    #     topic="Climate Change",
    #     native_state="Maharashtra, India"
    # )
    
    # # Example 3: Space exploration news for UK
    # print("\n\n🔹 Example 3: Space News\n")
    # run_news_report(
    #     topic="Space Exploration",
    #     native_state="London, UK"
    # )

# Made with Bob
